<div align="center">

<img src="assets/header.svg" width="100%" alt="Sri Sai Hemanth Bollepalli, medical AI researcher, with an animated brain MRI segmentation" />

<a href="https://github.com/sshemanth">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=17&duration=3200&pause=1000&color=4F8CFF&center=true&vCenter=true&width=640&lines=3D+brain+metastasis+segmentation+with+nnU-Net;Resection+cavity+segmentation+with+Primus;Calibrated%2C+uncertainty-aware+ADMET+prediction;Open+to+PhD+positions+in+medical+AI" alt="Research focus" />
</a>

<p>
  <a href="https://www.linkedin.com/in/sshemanth/"><img src="https://img.shields.io/badge/LinkedIn-sshemanth-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0B1426" alt="LinkedIn" /></a>
  <a href="mailto:sshemanthofficial@gmail.com"><img src="https://img.shields.io/badge/Email-sshemanthofficial-EA4335?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0B1426" alt="Email" /></a>
  <a href="https://openreview.net/forum?noteId=swAAtfR82q"><img src="https://img.shields.io/badge/MICCAI_2026-Paper-8C1D40?style=for-the-badge&logo=openreview&logoColor=white&labelColor=0B1426" alt="MICCAI 2026 paper" /></a>
  <a href="https://doi.org/10.5281/zenodo.20997792"><img src="https://img.shields.io/badge/Zenodo-TRUST--ADMET-1682D4?style=for-the-badge&logo=zenodo&logoColor=white&labelColor=0B1426" alt="TRUST-ADMET on Zenodo" /></a>
</p>

</div>

I build reproducible AI methods for biomedical problems, mainly **3D medical image segmentation** and **trustworthy molecular property prediction**. I care about careful validation, failure analysis, calibration and uncertainty.

<img src="assets/highlights.svg" width="100%" alt="Highlights: TC Dice 0.715 on the hidden test set, 2.7 times better resection cavity Dice, AUROC 0.912 on external B3DB, 3 MICCAI manuscripts reviewed" />

<img src="assets/divider.svg" width="100%" alt="" />

## Research

### [Region-Aware ResEnc nnU-Net for multi-region brain metastasis segmentation](https://github.com/sshemanth/brain-tumor-segmentation)

My MICCAI 2026 BraTS-METS challenge work with team Core_Neuro_AI, published as [*Region-Aware Residual Encoder nnU-Net for Multi-Region Brain Metastasis Segmentation*](https://openreview.net/forum?noteId=swAAtfR82q). It segments four regions from MRI: whole tumor (WT), tumor core (TC), enhancing tumor (ET) and resection cavity (RC).

Hidden test set, best single ResEnc-L model:

| | TC | ET | WT | RC |
|---|:---:|:---:|:---:|:---:|
| Lesion-wise Dice | 0.715 | 0.691 | 0.645 | 0.567 |

- Built on nnU-Net v2 with a Residual Encoder (Large) network.
- Designed a region-aware Tversky + BCE loss for rare regions such as RC.
- Found and fixed a class-order bug in region reconstruction.
- Tuned post-processing per region (RC threshold and minimum cavity size).

### [Primus transformer for resection cavities](https://github.com/sshemanth/brats-mets-primus-rc)

RC was the weakest region, so I trained a Primus transformer with cavity-focused sampling and compared it with standard nnU-Net on the same 260 cases.

<img src="assets/primus-rc.svg" width="100%" alt="Bar chart. Standard nnU-Net Dice: WT 0.747, TC 0.752, ET 0.721, RC 0.184. Primus with RC sampling: WT 0.760, TC 0.767, ET 0.734, RC 0.495." />

- RC Dice went from 0.18 to 0.50, about 2.7 times better.
- Most remaining errors are missed medium-sized cavities.
- Standard data splits leaked patients between train and test, so I built patient-grouped splits.
- Next step: use the patient's earlier scan to guide cavity segmentation.

### [TRUST-ADMET: trustworthy molecular property prediction](https://github.com/sshemanth/trust-admet)

A framework that reports how accurate a prediction is and whether it can be trusted. Version 1.0.1 is archived on [Zenodo](https://doi.org/10.5281/zenodo.20997792).

| Evaluation | Best model | Result |
|---|---|---|
| BBBP, scaffold split, 5 seeds | Random Forest | AUROC 0.874 ± 0.005, AUPRC 0.951 ± 0.002, ECE 0.061 ± 0.016 |
| ClinTox, scaffold split, 5 seeds | GIN | AUROC 0.844 ± 0.019 |
| Lipophilicity, scaffold split, 5 seeds | GIN | RMSE 0.748 ± 0.012, R² 0.604 ± 0.013 |
| B3DB external validation (N = 6,482) | Random Forest | AUROC 0.912, AUPRC 0.941 |

- Compared six model types (Random Forest, XGBoost, MLP, GCN, GIN, ChemBERTa) on scaffold splits.
- Added calibration, applicability domain, conformal prediction and uncertainty estimates.
- Validated on an external dataset after removing overlapping molecules.
- Packaged as software with a CLI, API, web demo and Docker image, under the MIT License.

<img src="assets/divider.svg" width="100%" alt="" />

## Research interests

- Robust medical image segmentation
- Small-lesion detection and post-surgery or follow-up MRI
- Uncertainty, calibration and failure analysis
- Trustworthy machine learning for drug discovery

## Tools

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch" />
  <img src="https://img.shields.io/badge/nnU--Net_v2-1E3A5F?style=flat-square" alt="nnU-Net v2" />
  <img src="https://img.shields.io/badge/PyTorch_Geometric-3C2179?style=flat-square&logo=pyg&logoColor=white" alt="PyTorch Geometric" />
  <img src="https://img.shields.io/badge/RDKit-0B5394?style=flat-square" alt="RDKit" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/XGBoost-189FDD?style=flat-square" alt="XGBoost" />
  <img src="https://img.shields.io/badge/Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face Transformers" />
  <img src="https://img.shields.io/badge/SimpleITK-2C5F2D?style=flat-square" alt="SimpleITK" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Google Cloud" />
</p>

<img src="assets/divider.svg" width="100%" alt="" />

<div align="center">

### Contact

I'm open to PhD positions and research collaborations in medical AI, biomedical image analysis and trustworthy AI.

[sshemanthofficial@gmail.com](mailto:sshemanthofficial@gmail.com) · [LinkedIn](https://www.linkedin.com/in/sshemanth/)

</div>
