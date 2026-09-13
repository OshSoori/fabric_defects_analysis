# fabric_defects_analysis# 🧵 Fabric Defect & Quality AI Analytics Pipeline

An enterprise-grade Data & AI solution built for quality assurance and predictive defect analytics in apparel manufacturing. This project implements a **Medallion Data Architecture** (Bronze → Silver → Gold), a machine learning classification engine for defect forecasting, and an interactive **Streamlit** executive dashboard.

---

## 📌 Business Overview & Problem Statement
Manual fabric quality inspections in garment manufacturing often lead to reactive defect handling, inconsistent quality scoring, and high material scrap costs. 

This project solves this operational bottleneck by automating quality data ingestion, structuring raw inspection logs into clean analytical layers, computing financial KPIs, and deploying a Machine Learning classifier to predict defective batches based on material physical parameters (e.g., GSM, tensile strength).

### **Key Business Outcomes**
* **Scrap Cost Reduction:** Identifies high-cost defect categories and poor-performing production lines.
* **Proactive Defect Prediction:** Replaces manual inspection delay with a predictive classifier.
* **Executive Visibility:** Translates technical data metrics into real-time operational financial KPIs.

---

## 🏗️ Technical Architecture (Medallion Framework)

```text
[ Raw Inspection & Sensor Data ]
               │
               ▼ (Data Generation & Ingestion)
       ┌───────────────┐
       │  BRONZE LAYER │  --> Raw Inspection Logs (data/raw_inspection_logs.csv)
       └───────┬───────┘
               │
               ▼ (ETL, Cleaning & Feature Engineering)
       ┌───────────────┐
       │  SILVER LAYER │  --> Cleaned & Formatted Data (data/silver_inspections.csv)
       └───────┬───────┘
               │
       ┌───────┴─────────────────────────────┐
       ▼                                     ▼
┌───────────────┐                 ┌───────────────────┐
│   GOLD LAYER  │                 │    ML ENGINE      │
│ Aggregated    │                 │ RandomForest /    │
│ Business KPIs │                 │ XGBoost Model     │
└───────┬───────┘                 └─────────┬─────────┘
        │                                   │
        └─────────────────┬─────────────────┘
                          ▼
            [ Streamlit BI Dashboard ]
