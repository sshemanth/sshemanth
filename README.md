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

`GNNs` `ChemBERTa` `calibration` `applicability domain` `FastAPI` `Docker`

Most ADMET repositories report only AUROC or RMSE. TRUST-ADMET also answers whether a single prediction can be trusted, by checking calibration, applicability domain, uncertainty and explainability. v1.0.1 is archived on [Zenodo](https://doi.org/10.5281/zenodo.20997792).

<img src="assets/trust-framework.svg" width="100%" alt="TRUST-ADMET framework: molecules become fingerprints, graphs or SMILES tokens; six model families train on random and scaffold splits; a trust layer adds calibration, applicability domain, uncertainty and explainability; results ship as a CLI, API, Gradio app and Docker image." />

Six model families compared (RF, XGBoost, MLP, GCN, GIN, ChemBERTa) on scaffold splits across five seeds:

| Dataset (scaffold split) | Best model | Result |
|---|---|---|
| BBBP | Random Forest | AUROC 0.874 ± 0.005, AUPRC 0.951 ± 0.002, ECE 0.061 ± 0.016 |
| ClinTox | GIN | AUROC 0.844 ± 0.019 |
| Lipophilicity | GIN | RMSE 0.748 ± 0.012, R² 0.604 ± 0.013 |
| B3DB external validation (N = 6,482) | Random Forest | AUROC 0.912, AUPRC 0.941 |

A molecule outside the training chemical space is far less reliable, and the framework flags it. Random Forest AUROC inside vs outside the applicability domain:

<img src="assets/trust-ad.svg" width="100%" alt="Random Forest test AUROC inside vs outside the applicability domain: BBBP 0.943 vs 0.801, ClinTox 0.909 vs 0.706, Tox21 NR-AR 0.812 vs 0.718, Tox21 SR-p53 0.830 vs 0.716." />

<img src="https://raw.githubusercontent.com/sshemanth/trust-admet/main/paper/figures/Figure6_GIN_GNNExplainer.png" width="60%" alt="GNNExplainer highlighting the atoms a GIN model used for a molecular property prediction." />

Explainability check: GNNExplainer marks the atoms a GIN model relied on. Everything ships as a CLI, FastAPI service, Gradio demo and Docker image under the MIT License.

### [Multi-label knee MRI abnormality detection from report-derived labels](https://github.com/sshemanth/knee-mri-weak-supervision)

`RSNA 2026 knee MRI` `weak supervision` `LLM labelling` `ConvNeXt` `team of 2`

Detects 12 knee abnormalities on MRI without any expert image labels. Three report readers (regex, MedGemma-4B and a locally served Qwen 27B) score the radiology reports, and their average becomes the training labels. **0.880 macro AUC on the hidden test set**, 0.863 on 58 expert-labelled studies.

<img src="assets/knee-pipeline.svg" width="100%" alt="Knee MRI pipeline: reports scored by regex (0.683), MedGemma-4B (0.768) and Qwen 27B (0.858), fused into soft labels (0.870), which supervise a 2.5D ConvNeXt-Tiny with per-finding attention reaching 0.880 macro AUC on the hidden test." />

<img src="https://raw.githubusercontent.com/sshemanth/knee-mri-weak-supervision/main/figures/fig1_inputs.png" width="100%" alt="The five MRI views the model reads: sagittal fluid-sensitive, sagittal other, coronal fluid-sensitive, coronal other and axial." />

<table>
<tr>
<td width="55%"><img src="https://raw.githubusercontent.com/sshemanth/knee-mri-weak-supervision/main/figures/fig2_auc_per_finding.png" alt="Per-finding ROC AUC with 95% bootstrap confidence intervals on 58 expert-labelled studies; macro 0.863. Highest: Baker's cyst and medial OA 0.97; lowest: MCL 0.69." /></td>
<td width="45%"><img src="https://raw.githubusercontent.com/sshemanth/knee-mri-weak-supervision/main/figures/fig3_ACL.png" alt="ACL: slices the model weighted most, for a correct detection, a missed case and a false alarm." /></td>
</tr>
<tr>
<td><sub>Per-finding AUC with 95% bootstrap CIs on the 58 expert-labelled studies.</sub></td>
<td><sub>ACL: the slices the model's attention weighted most, for a hit, a miss and a false alarm.</sub></td>
</tr>
</table>

- Better labels gave the biggest gain: adding the Qwen reader raised the hidden-test AUC from 0.842 to 0.865, more than a larger image model did.
- The attention maps show the model leans on sagittal fluid-sensitive images, even for the MCL, which radiologists read on coronal images.

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
