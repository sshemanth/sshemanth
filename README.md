<div align="center">

<img src="assets/header.svg" width="100%" alt="Sri Sai Hemanth Bollepalli. Medical AI and trustworthy machine learning researcher, Master of AI at UTS Sydney, MICCAI 2026 BraTS-METS paper accepted, open to PhD positions. Animated nnU-Net encoder-decoder diagram." />

<a href="https://github.com/sshemanth">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=16&duration=3000&pause=900&color=4F8CFF&center=true&vCenter=true&width=720&lines=3D+brain+metastasis+segmentation+with+nnU-Net+and+Primus;Calibrated%2C+uncertainty-aware+molecular+property+prediction;LLM+pipelines+for+medical+report+labelling;From+raw+scans+to+released%2C+reproducible+software" alt="Research focus" />
</a>

<p>
  <a href="https://openreview.net/forum?noteId=swAAtfR82q"><img src="https://img.shields.io/badge/MICCAI_2026-paper_accepted-C0841C?style=for-the-badge&labelColor=0B1426" alt="MICCAI 2026 paper accepted" /></a>
  <a href="https://doi.org/10.5281/zenodo.20997792"><img src="https://img.shields.io/badge/Zenodo-TRUST--ADMET_v1.0.1-1682D4?style=for-the-badge&logo=zenodo&logoColor=white&labelColor=0B1426" alt="TRUST-ADMET on Zenodo" /></a>
  <a href="https://www.linkedin.com/in/sshemanth/"><img src="https://img.shields.io/badge/LinkedIn-sshemanth-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B1426" alt="LinkedIn" /></a>
  <a href="mailto:sshemanthofficial@gmail.com"><img src="https://img.shields.io/badge/Email-sshemanthofficial-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B1426" alt="Email" /></a>
</p>

</div>

I build medical AI end to end: data pipelines, 3D segmentation and graph models, LLM labelling, uncertainty and calibration, and the software that ships it. My BraTS-METS 2026 challenge entry was solo, with no supervisor, and the paper was accepted at MICCAI 2026.

<img src="assets/highlights.svg" width="100%" alt="Highlights: TC lesion-wise Dice 0.715 on the BraTS-METS 2026 hidden test; 2.7 times better resection cavity Dice with Primus; AUROC 0.912 on external B3DB; 0.88 macro AUC on knee MRI." />

<img src="assets/divider.svg" width="100%" alt="" />

## How I work

<img src="assets/pipeline.svg" width="100%" alt="Research pipeline in six stages: data, prepare, model, validate, trust, ship." />

## Capability stack

<img src="assets/stack.svg" width="100%" alt="Capability stack in six layers: medical AI, research, LLMs and agents, deep learning, machine learning, infrastructure." />

<img src="assets/divider.svg" width="100%" alt="" />

## Selected work

### [Region-Aware ResEnc nnU-Net for multi-region brain metastasis segmentation](https://github.com/sshemanth/brain-tumor-segmentation)

`MICCAI 2026 BraTS-METS` `nnU-Net v2` `3D MRI` `solo entry`

My challenge work, published as [*Region-Aware Residual Encoder nnU-Net for Multi-Region Brain Metastasis Segmentation*](https://openreview.net/forum?noteId=swAAtfR82q). It segments whole tumor (WT), tumor core (TC), enhancing tumor (ET) and resection cavity (RC) from multi-sequence MRI.

| Hidden test set, lesion-wise Dice | TC | ET | WT | RC |
|---|:---:|:---:|:---:|:---:|
| Best single ResEnc-L model | 0.715 | 0.691 | 0.645 | 0.567 |

- Region-aware Tversky + BCE loss for rare regions such as RC.
- Found and fixed a class-order bug in region reconstruction.
- Per-region post-processing (RC threshold and minimum cavity size).

### [Primus transformer for resection cavities](https://github.com/sshemanth/brats-mets-primus-rc)

`vision transformer` `cavity-focused sampling` `error analysis`

<img src="assets/primus-rc.svg" width="100%" alt="Standard nnU-Net Dice: WT 0.747, TC 0.752, ET 0.721, RC 0.184. Primus with RC sampling: WT 0.760, TC 0.767, ET 0.734, RC 0.495." />

- Most remaining errors are missed medium-sized cavities.
- Standard splits leaked patients between train and test, so I built patient-grouped splits.

### [TRUST-ADMET: trustworthy molecular property prediction](https://github.com/sshemanth/trust-admet)

`GNNs` `ChemBERTa` `conformal prediction` `calibration` `Docker`

Reports how accurate a prediction is and whether it can be trusted. v1.0.1 is archived on [Zenodo](https://doi.org/10.5281/zenodo.20997792).

| Evaluation | Best model | Result |
|---|---|---|
| BBBP, scaffold split, 5 seeds | Random Forest | AUROC 0.874 ± 0.005, AUPRC 0.951 ± 0.002, ECE 0.061 ± 0.016 |
| ClinTox, scaffold split, 5 seeds | GIN | AUROC 0.844 ± 0.019 |
| Lipophilicity, scaffold split, 5 seeds | GIN | RMSE 0.748 ± 0.012, R² 0.604 ± 0.013 |
| B3DB external validation (N = 6,482) | Random Forest | AUROC 0.912, AUPRC 0.941 |

Six model families compared (RF, XGBoost, MLP, GCN, GIN, ChemBERTa), with applicability domain checks, external validation after removing overlapping molecules, and a CLI, API, web demo and Docker image under the MIT License.

### Multi-label knee MRI abnormality detection from report-derived labels

`RSNA knee MRI` `weak supervision` `Qwen` `MedGemma` `team of 2`

Detects 12 findings from knee MRI, trained on labels pulled from radiology reports instead of manual annotation. Reached **0.88 macro AUC**. For labelling, a local Qwen model scored 0.858 macro AUC on 58 gold-standard reports, matching my regex + MedGemma fusion (0.857).

### AeroTail: deep RL drone target following

`SAC` `PPO` `AirSim` `team project`

Autonomous visual target-following drone trained with deep reinforcement learning in AirSim. I ran the SAC and PPO experiments.

### In progress

- Lesion-level conformal guarantees for post-treatment brain metastasis segmentation.
- Explainable atrial fibrillation detection from 12-lead ECG, trained on PTB-XL and tested on Chapman-Shaoxing.

<img src="assets/divider.svg" width="100%" alt="" />

## Timeline

<img src="assets/timeline.svg" width="100%" alt="Timeline as a git log, from a B.Tech in Computer Science (2020 to 2024) to the Master of AI at UTS, projects in 2026 and current research." />

## Activity

<img src="assets/github-stats.svg" width="100%" alt="GitHub activity over the last 12 months, updated daily by a GitHub Action." />

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="assets/snake-light.svg" />
  <img src="assets/snake-dark.svg" width="100%" alt="Contribution graph animation" />
</picture>

<img src="assets/divider.svg" width="100%" alt="" />

<div align="center">

### Contact

Open to PhD positions and research collaborations in medical AI, biomedical image analysis and trustworthy AI.

[sshemanthofficial@gmail.com](mailto:sshemanthofficial@gmail.com) · [LinkedIn](https://www.linkedin.com/in/sshemanth/)

<sub>Stats and contribution graph regenerate daily via <code>.github/workflows/profile.yml</code></sub>

</div>
