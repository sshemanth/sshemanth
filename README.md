# Sri Sai Hemanth Bollepalli

**Medical AI & Trustworthy Machine Learning Researcher**  
Master of Artificial Intelligence candidate, University of Technology Sydney (UTS) — expected November 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sshemanth/)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?logo=gmail&logoColor=white)](mailto:srisaihemanth.bollepalli@student.uts.edu.au)

I build reproducible AI methods for biomedical problems, focusing on **3D medical image segmentation** and **trustworthy molecular property prediction**. I care about careful validation, failure analysis, calibration and uncertainty.

- 🧠 **MICCAI 2026 BraTS-METS Challenge** participant (team Core_Neuro_AI) and challenge reviewer (3 manuscripts)
- 💊 **TRUST-ADMET v1.0.1** released and archived on [Zenodo](https://doi.org/10.5281/zenodo.20997792)

## Active research

### [LAResSeg — Lesion-Aware Brain Metastasis Segmentation](https://github.com/sshemanth/brain-tumor-segmentation)

Segmentation of four brain-metastasis regions from MRI: whole tumor (WT), tumor core (TC), enhancing tumor (ET) and **resection cavity (RC)**. This is my BraTS-METS 2026 challenge work.

**Hidden test set** (best single ResEnc-L model, lesion-wise Dice):

| | TC | ET | WT | RC |
|---|---:|---:|---:|---:|
| Lesion-wise Dice | **0.715** | **0.691** | **0.645** | **0.567** |

**What I did**

- Built on **nnU-Net v2** with a Residual Encoder (Large) network.
- Designed a **region-aware Tversky + BCE loss** for rare regions such as RC.
- Found and fixed a class-order bug in region reconstruction.
- Tuned post-processing per region (RC threshold and minimum cavity size).

### [Follow-up: Primus transformer for resection cavities](https://github.com/sshemanth/brats-mets-primus-rc)

RC was the weakest region, so I trained a **Primus** transformer with **cavity-focused sampling**. Compared with the **standard nnU-Net** on the same 260 cases:

| Model | WT | TC | ET | RC |
|---|---:|---:|---:|---:|
| Standard nnU-Net | 0.747 | 0.752 | 0.721 | 0.184 |
| **Primus + RC sampling** | **0.760** | **0.767** | **0.734** | **0.495** |

- **RC Dice: 0.18 → 0.50** (about 2.7× better).
- Found that most errors are **missed medium-sized cavities**.
- Found **patient leakage** in standard data splits and made patient-grouped splits.
- **Next:** use the patient's **earlier scan** to guide cavity segmentation.

---

### [TRUST-ADMET — Trustworthy AI for Molecular Property Prediction](https://github.com/sshemanth/trust-admet)

A framework that checks both **how accurate** a prediction is and **whether it can be trusted**.

| Evaluation | Best model | Result |
|---|---|---|
| BBBP scaffold-split test, 5 seeds | Random Forest | AUROC **0.874 ± 0.005**; AUPRC **0.951 ± 0.002**; ECE **0.061 ± 0.016** |
| ClinTox scaffold-split test, 5 seeds | GIN | AUROC **0.844 ± 0.019** |
| Lipophilicity scaffold-split test, 5 seeds | GIN | RMSE **0.748 ± 0.012**; R² **0.604 ± 0.013** |
| B3DB external validation, N = 6,482 | Random Forest | AUROC **0.912**; AUPRC **0.941** |

**What I did**

- Compared six model types (Random Forest, XGBoost, MLP, GCN, GIN, ChemBERTa) with scaffold splits.
- Added calibration, applicability domain, conformal prediction and uncertainty estimates.
- Tested on an external dataset after removing overlapping molecules.
- Released it as software: CLI, API, web demo and Docker, under the MIT License.

## Research interests

- Robust medical image segmentation
- Small-lesion detection and post-surgery / follow-up MRI
- Uncertainty, calibration and failure analysis
- Trustworthy machine learning for drug discovery

## Tools

**Python · PyTorch · nnU-Net v2 · PyTorch Geometric · RDKit · scikit-learn · XGBoost · Transformers · SimpleITK · Docker · GCP**

## Let's connect

I'm open to **PhD opportunities** and **research collaboration** in medical AI, biomedical image analysis and trustworthy AI.

**Contact:** [srisaihemanth.bollepalli@student.uts.edu.au](mailto:srisaihemanth.bollepalli@student.uts.edu.au) · [LinkedIn](https://www.linkedin.com/in/sshemanth/)
