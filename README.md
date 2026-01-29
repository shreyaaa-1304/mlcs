Malicious URL Detection — Project Documentation
Purpose

To document the problem definition, dataset, feature engineering approach, modeling strategy, evaluation metrics, and the process used to update and refine a supervised machine learning system for malicious URL detection.

1) Problem Overview

The objective of this project is to perform binary classification of URLs into malicious or legitimate categories.
The system aims to achieve high detection accuracy with low inference latency to enable early identification and blocking of harmful web links in real-world environments.

2) Goals & Success Criteria
Primary Goals

Classification Accuracy ≥ 90%

F1-score (malicious class) ≥ 0.88

Inference latency < 1 second per URL (p95)

Secondary Goals

False Positive Rate (legitimate → malicious) ≤ 1%

Stable performance across unseen and newly generated URLs

3) Data Summary
Data Sources

PhishTank

OpenPhish

Public malicious URL datasets (Kaggle)

Data Format

CSV / JSON

Dataset Versioning

Dataset details, schema, and class distribution are documented in DATASET_CARD.md

Bias & Privacy Considerations

No personally identifiable information (PII) is collected

URLs from diverse domains and regions are included

Data usage complies with source terms and conditions

4) Feature Engineering (Current Plan)
URL-based Lexical Features

Total URL length

Count of digits, dots, hyphens, and special characters

Subdomain depth

Presence of IP address instead of domain name

Detection of suspicious keywords (e.g., login, secure, verify)

Optional Enrichment (Future Scope)

Domain age and registration metadata

Reputation scores from public blacklists

5) Modeling Approach
Baseline Models

Logistic Regression

Decision Tree

Advanced Models

Random Forest

Gradient Boosting (e.g., LightGBM)

Explainability

Feature importance analysis

SHAP values for model interpretability

Model Tracking

Each trained model version is logged in MODEL_CARD.md

6) Evaluation Strategy
Offline Evaluation Metrics

Accuracy

Precision

Recall

F1-score (overall and malicious class)

ROC-AUC

Operational Metrics (Post-deployment Simulation)

False positive rate

Detection consistency on new URL batches

Experiment Tracking

All experiment results and comparisons are recorded in EVAL_LOG.md

7) Versioning & Refinement Workflow
Version Control

Git is used for source code and documentation

Documentation Files

DATASET_CARD.md — dataset versions, size, class balance, known limitations

MODEL_CARD.md — model configurations, features, metrics, latency

EVAL_LOG.md — experiment results, confusion matrices, evaluation scores

CHANGELOG.md — summary of updates and improvements

FEEDBACK_LOG.md — issues and feedback with resolution status

Update Cadence

Weekly: Feature tuning, bug fixes, evaluation updates

Bi-weekly: Dataset refresh and optional retraining

Monthly: Performance review and documentation updates

Refinement Triggers

F1-score (malicious class) drops below 0.88

Significant data drift detected in URL features

Increase in false positive reports

Latency exceeds defined thresholds

Update Procedure

Create a new Git branch:
docs/update-YYYY-MM-DD-description

Modify relevant documentation and code files

Record before-and-after performance metrics in EVAL_LOG.md

Merge changes and update version numbers

Append summary to CHANGELOG.md

8) Reproducibility

Random seed fixed to 42

Configuration files stored in configs/

Each experiment records:

Dataset version

Feature list

Model parameters

Commit hash

Execution environment

9) Ethics & Risk Considerations

False positives are minimized to avoid blocking legitimate websites

Automated decisions are documented and explainable

The system is intended to assist, not replace, security decision-makers

10) Architecture & Workflow

High-level pipeline:

URL Ingestion → Feature Extraction → ML Model → Classification Decision


Detailed workflow diagrams are available in docs/workflow.md.

Summary

This project implements a supervised machine learning–based approach for detecting malicious URLs using lightweight lexical features. The system is designed to be accurate, efficient, explainable, and adaptable to evolving web threats, making it suitable for further experimentation and real-world security applications.
