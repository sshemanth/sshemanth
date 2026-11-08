"""Build assets/github-stats.svg from the GitHub GraphQL API.

Runs in GitHub Actions (see .github/workflows/profile.yml) with GITHUB_TOKEN.
Local test: python scripts/stats.py --demo
"""
import json, os, sys, urllib.request, html
from collections import Counter

USER = os.environ.get("GH_USER", "sshemanth")
OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "github-stats.svg")

BG, CARD, LINE = "#0C1830", "#0F1D36", "#22345A"
INK, MUTED = "#E6EDF7", "#9FB2CC"
BLUE = "#4F8CFF"
LANG_COLS = ["#4F8CFF", "#1F9E8F", "#C0841C", "#D9536B", "#8E7CF0", "#6B7A90"]
SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "Georgia, 'Times New Roman', serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

QUERY = """
query($login:String!){ user(login:$login){
  followers{totalCount}
  contributionsCollection{
    totalCommitContributions
    contributionCalendar{ totalContributions weeks{ contributionDays{ contributionCount } } }
  }
  repositories(ownerAffiliations:OWNER, isFork:false, privacy:PUBLIC, first:100){
    totalCount
    nodes{ languages(first:8, orderBy:{field:SIZE,direction:DESC}){ edges{ size node{ name } } } }
  }
}}"""


def fetch():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": USER}}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        d = json.load(r)
    if "errors" in d:
        sys.exit(f"GraphQL error: {d['errors']}")
    u = d["data"]["user"]
    cc = u["contributionsCollection"]
    cal = cc["contributionCalendar"]["weeks"]
    weeks = [sum(day["contributionCount"] for day in w["contributionDays"]) for w in cal]
    active = sum(1 for w in cal for day in w["contributionDays"] if day["contributionCount"] > 0)
    langs = Counter()
    for n in u["repositories"]["nodes"]:
        for e in n["languages"]["edges"]:
            langs[e["node"]["name"]] += e["size"]
    return {
        "contrib": cc["contributionCalendar"]["totalContributions"],
        "commits": cc["totalCommitContributions"],
        "repos": u["repositories"]["totalCount"],
        "active": active,
        "weeks": weeks,
        "langs": langs.most_common(),
    }


def render(s):
    W, H = 1200, 300
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" '
           f'aria-label="GitHub activity: {s["contrib"]} contributions in the last year, {s["commits"]} commits, '
           f'{s["repos"]} public repositories, {s["active"]} active days.">',
           "<style>.up{opacity:0;animation:up .7s cubic-bezier(.2,.7,.2,1) forwards}"
           "@keyframes up{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}"
           ".bar{transform-box:fill-box;transform-origin:bottom;transform:scaleY(0);animation:g .8s cubic-bezier(.2,.8,.2,1) forwards}"
           "@keyframes g{to{transform:scaleY(1)}}"
           "@media (prefers-reduced-motion: reduce){*{animation:none!important}.up{opacity:1}.bar{transform:none}}</style>",
           f'<rect width="{W}" height="{H}" rx="18" fill="{BG}" stroke="{LINE}"/>',
           f'<text x="30" y="40" font-family="{MONO}" font-size="13" fill="#7FA6E0">gh api graphql · updated daily</text>',
           f'<text x="30" y="64" font-family="{SANS}" font-size="19" font-weight="700" fill="{INK}">GitHub activity, last 12 months</text>']
    tiles = [(s["contrib"], "contributions"), (s["commits"], "commits"), (s["repos"], "public repos"), (s["active"], "active days")]
    for i, (v, lab) in enumerate(tiles):
        x, y = 30 + (i % 2) * 170, 88 + (i // 2) * 96
        out.append(f'<g class="up" style="animation-delay:{.1+i*.1:.1f}s"><rect x="{x}" y="{y}" width="158" height="84" rx="12" fill="{CARD}" stroke="{LINE}"/>'
                   f'<text x="{x+16}" y="{y+42}" font-family="{SERIF}" font-size="30" fill="{INK}">{v:,}</text>'
                   f'<text x="{x+16}" y="{y+66}" font-family="{SANS}" font-size="13" fill="{MUTED}">{lab}</text></g>')
    # weekly bars
    wk = s["weeks"][-52:]
    mx = max(wk) or 1
    x0, x1, base, top = 400, 860, 260, 104
    bw = (x1 - x0) / len(wk)
    out.append(f'<text x="{x0}" y="96" font-family="{SANS}" font-size="13" fill="{MUTED}">contributions per week</text>')
    out.append(f'<line x1="{x0}" x2="{x1}" y1="{base}" y2="{base}" stroke="#3A4E74"/>')
    for i, v in enumerate(wk):
        h = max(2, (v / mx) * (base - top - 10)) if v else 0
        if h:
            out.append(f'<rect class="bar" style="animation-delay:{.3+i*.012:.3f}s" x="{x0+i*bw+1:.1f}" y="{base-h:.1f}" '
                       f'width="{bw-2:.1f}" height="{h:.1f}" rx="1.5" fill="{BLUE}"/>')
    out.append(f'<text x="{x0}" y="{base+20}" font-family="{SANS}" font-size="12" fill="{MUTED}">12 months ago</text>')
    out.append(f'<text x="{x1}" y="{base+20}" text-anchor="end" font-family="{SANS}" font-size="12" fill="{MUTED}">this week · peak {mx}</text>')
    # languages
    langs = s["langs"][:5]
    total = sum(v for _, v in s["langs"]) or 1
    rest = total - sum(v for _, v in langs)
    if rest > 0:
        langs.append(("Other", rest))
    lx, ly, lw = 900, 104, 270
    out.append(f'<text x="{lx}" y="96" font-family="{SANS}" font-size="13" fill="{MUTED}">languages across public repos</text>')
    cx = lx
    for i, (n, v) in enumerate(langs):
        w = lw * v / total
        out.append(f'<rect class="up" style="animation-delay:{.4+i*.08:.2f}s" x="{cx:.1f}" y="{ly}" width="{max(w-2,1):.1f}" height="10" rx="3" fill="{LANG_COLS[i]}"/>')
        cx += w
    for i, (n, v) in enumerate(langs):
        y = ly + 40 + i * 22
        out.append(f'<g class="up" style="animation-delay:{.5+i*.08:.2f}s"><rect x="{lx}" y="{y-9}" width="10" height="10" rx="3" fill="{LANG_COLS[i]}"/>'
                   f'<text x="{lx+18}" y="{y}" font-family="{SANS}" font-size="13" fill="{INK}">{html.escape(n)}</text>'
                   f'<text x="{lx+lw}" y="{y}" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{MUTED}">{100*v/total:.1f}%</text></g>')
    out.append("</svg>")
    return "".join(out)


if __name__ == "__main__":
    if "--demo" in sys.argv:
        import random
        data = {"contrib": 812, "commits": 640, "repos": 14, "active": 120,
                "weeks": [random.randint(0, 40) for _ in range(53)],
                "langs": [("Python", 900), ("Jupyter Notebook", 500), ("TypeScript", 200), ("Shell", 60), ("HTML", 40), ("CSS", 20)]}
        out = os.path.join(os.path.dirname(__file__), "..", "_demo-stats.svg")
    else:
        data, out = fetch(), OUT
    with open(out, "w") as f:
        f.write(render(data))
    print("wrote", out)
