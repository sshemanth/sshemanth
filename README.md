# Sri Sai Hemanth Bollepalli

**Medical AI & Trustworthy Machine Learning Researcher**  
Master of Artificial Intelligence candidate, University of Technology Sydney (UTS) — expected November 2026

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sshemanth/)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?logo=gmail&logoColor=white)](mailto:srisaihemanth.bollepalli@student.uts.edu.au)

I develop reproducible AI methods for biomedical problems, with a current focus on **lesion-aware 3D medical image segmentation** and **trustworthy molecular property prediction**. My work emphasizes rigorous validation, failure analysis, calibration, uncertainty, and practical research software.

## Active research

### [LAResSeg — Lesion-Aware Brain Metastasis Segmentation](https://github.com/sshemanth/brain-tumor-segmentation)

> **Hidden-test result:** the best single **ResEncL V3** model (fold 0) achieved lesion-wise Dice scores of **0.7154 TC**, **0.6905 ET**, **0.6453 WT**, and **0.5674 RC** on the BraTS-MET Synapse hidden test set, with **0.6458 RC all-instance F1**.

| Hidden-test metric | TC | ET | WT | RC |
|---|---:|---:|---:|---:|
| Lesion-wise Dice | **0.7154** | **0.6905** | **0.6453** | **0.5674** |

I am developing a multi-region 3D MRI framework for whole tumor (WT), tumor core (TC), enhancing tumor (ET), and postoperative resection cavity (RC) segmentation from T1, T1c, T2, and FLAIR MRI.

**Technical contributions**

- Adapted **nnU-Net v2** to a Residual Encoder Large backbone for multi-region metastasis and cavity segmentation.
- Designed an **asymmetric region Tversky + BCE loss** to address severe lesion and RC class imbalance.
- Established correct hierarchical region reconstruction and full-volume validation after identifying a fragile class-order failure mode.
- Tuned region-specific post-processing; the best tested single-model setting uses an **RC probability threshold of 0.15** and a **200-voxel minimum component size**.
- Demonstrated that unified multi-task learning outperformed RC-only binary variants; remaining folds and ensemble ablations are in progress.

**Publication focus:** lesion-aware loss design, rare-region failure analysis, small-lesion sensitivity, and hidden-test generalization in heterogeneous multi-modal MRI.

---

### [TRUST-ADMET — Trustworthy AI for Molecular Property Prediction](https://github.com/sshemanth/trust-admet)

> **External-validation result:** a BBBP-trained Random Forest achieved **0.912 AUROC**, **0.941 AUPRC**, **0.580 MCC**, and **0.087 ECE** on **6,482** B3DB molecules after removing **1,325** molecules overlapping the training set.

| Evaluation | Best model | Result |
|---|---|---|
| BBBP scaffold-split test, 5 seeds | Random Forest | AUROC **0.874 ± 0.005**; AUPRC **0.951 ± 0.002**; ECE **0.061 ± 0.016** |
| ClinTox scaffold-split test, 5 seeds | GIN | AUROC **0.844 ± 0.019** |
| Lipophilicity scaffold-split test, 5 seeds | GIN | RMSE **0.748 ± 0.012**; R² **0.604 ± 0.013** |
| B3DB external validation, N = 6,482 | Random Forest | AUROC **0.912**; AUPRC **0.941** |

TRUST-ADMET is an end-to-end framework that evaluates predictive performance together with whether an individual prediction should be trusted.

**Technical contributions**

- Benchmarked six model families—Random Forest, XGBoost, MLP, GCN, GIN, and ChemBERTa—across four classification and two regression endpoints using scaffold splits.
- Integrated probability calibration, similarity- and physicochemical-space applicability domains, conformal prediction, Monte Carlo dropout, ensemble disagreement, and model-specific explainability.
- Added overlap-controlled external validation to reduce train–test contamination when transferring BBBP models to B3DB.
- Built configuration-driven experiments, automated benchmark and paper-asset generation, a CLI, FastAPI service, Gradio interface, Docker deployment, and reproducible research packaging.
- Released the software as **v1.0.1** under the MIT License and archived it on Zenodo: [doi:10.5281/zenodo.20997792](https://doi.org/10.5281/zenodo.20997792).

**Publication focus:** connecting accuracy with calibration, applicability domain, uncertainty, explainability, and independent external validation across model families.

## Research interests

- Robust and generalizable medical image segmentation
- Small-lesion detection and postoperative MRI analysis
- Uncertainty quantification, calibration, and failure-aware AI
- Multimodal biomedical learning and clinical decision support
- Trustworthy machine learning for drug discovery

## Methods and tools

**Python · PyTorch · nnU-Net v2 · PyTorch Geometric · RDKit · scikit-learn · XGBoost · Transformers · SimpleITK · NiBabel · Docker · GCP**

## PhD and research collaboration

I welcome conversations about PhD supervision and research collaboration in **medical AI, biomedical image analysis, trustworthy AI, and molecular machine learning**. I am particularly interested in work that combines methodological novelty with careful validation and clinically or scientifically meaningful evaluation.

**Contact:** [srisaihemanth.bollepalli@student.uts.edu.au](mailto:srisaihemanth.bollepalli@student.uts.edu.au) · [LinkedIn](https://www.linkedin.com/in/sshemanth/)
