# Malicious URL Detection — Project Documentation

## Purpose
This document describes the problem definition, dataset, feature engineering approach, modeling strategy, evaluation metrics, and the process used to update and refine a supervised machine learning system for malicious URL detection.

---

## 1. Problem Overview
The objective of this project is to perform **binary classification** of URLs into **malicious** or **legitimate** categories.  
The system is designed to achieve high detection accuracy with low inference latency to support early identification and blocking of harmful web links.

---

## 2. Goals & Success Criteria

### Primary Goals
- Accuracy ≥ 90%
- F1-score (malicious class) ≥ 0.88
- Inference latency < 1 second per URL (p95)

### Secondary Goals
- False Positive Rate (legitimate → malicious) ≤ 1%
- Consistent performance on previously unseen URLs

---

## 3. Data Summary

### Data Sources
- PhishTank  
- OpenPhish  
- Public malicious URL datasets from Kaggle  

### Data Format
- CSV / JSON

### Dataset Versioning
- Dataset details including schema, size, and class balance are maintained in `DATASET_CARD.md`

### Bias & Privacy Considerations
- No personally identifiable information (PII) is collected  
- URLs from diverse domains and regions are included  
- Data usage complies with dataset terms and conditions  

---

## 4. Feature Engineering

### URL-Based Lexical Features
- Total URL length  
- Count of dots, digits, hyphens, and special characters  
- Subdomain depth  
- Use of IP address instead of a domain name  
- Presence of suspicious keywords (e.g., `login`, `secure`, `verify`)  

### Optional Enhancements (Future Scope)
- Domain age and registration metadata  
- Reputation scores from public blacklists  

---

## 5. Modeling Approach

### Baseline Models
- Logistic Regression  
- Decision Tree  

### Advanced Models
- Random Forest  
- Gradient Boosting (e.g., LightGBM)  

### Explainability
- Feature importance analysis  
- SHAP values for model interpretability  

### Model Tracking
- Model versions and training details are documented in `MODEL_CARD.md`

---

## 6. Evaluation Strategy

### Offline Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

### Operational Metrics
- False positive rate  
- Detection consistency on new URL batches  

### Experiment Tracking
- All experiments and results are recorded in `EVAL_LOG.md`

---

## 7. Versioning & Refinement Workflow

### Version Control
- Git is used for code and documentation management  

### Documentation Files
- `DATASET_CARD.md` — dataset schema, size, balance, and known issues  
- `MODEL_CARD.md` — model configurations, features, metrics, and latency  
- `EVAL_LOG.md` — experiment results and comparisons  
- `CHANGELOG.md` — summary of updates and improvements  
- `FEEDBACK_LOG.md` — feedback, issues, and resolution status  

### Update Cadence
- **Weekly**: Feature tuning and evaluation updates  
- **Bi-weekly**: Dataset refresh and model retraining (if required)  
- **Monthly**: Performance review and documentation updates  

### Refinement Triggers
- F1-score (malicious class) falls below 0.88  
- Significant drift detected in URL features  
- Increase in false positive reports  
- Latency exceeds defined thresholds  

---

## 8. Reproducibility
- Random seed fixed to 42  
- Configuration files stored in `configs/`  
- Each experiment records:
  - Dataset version  
  - Feature list  
  - Model parameters  
  - Commit hash  
  - Execution environment  

---

## 9. Ethics & Risk Considerations
- False positives are minimized to avoid blocking legitimate websites  
- Automated decisions remain explainable and transparent  
- The system assists security analysts rather than replacing human judgment  

---

## 10. Architecture & Workflow

### High-Level Pipeline
