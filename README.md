
# 🧵 Fabric Defect & Quality AI Analytics Pipeline

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

```



 * Bronze Layer (data/raw_inspection_logs.csv): Stores raw inspection logs including timestamp, batch ID, line ID, fabric type, GSM, tensile strength, and defect counts.
 * Silver Layer (data/silver_inspections.csv): Cleans missing records, formats target variables (is_defective), and derives financial impact metrics (scrap_cost_usd).
 * Gold Layer (data/gold_kpis.csv): Aggregates executive KPIs, calculating defect rates (%) and total yield loss grouped by line ID and fabric weave.
 * Machine Learning Model (src/model.py): Trains a supervised classifier to evaluate batch defect risk based on manufacturing properties.
## 🗂️ Project Repository Structure 

```text

fabric_defects_analysis/
├── dashboard/
│   └── app.py                  # Interactive Streamlit dashboard UI
├── data/
│   ├── raw_inspection_logs.csv  # Bronze data layer
│   ├── silver_inspections.csv  # Silver data layer
│   └── gold_kpis.csv           # Gold data layer
├── src/
│   ├── genarate_data.py        # Synthetic dataset generator script
│   ├── pipeline.py             # Medallion ETL data transformation script
│   ├── model.py                # Machine learning training engine
│   └── defect_classifier.pkl   # Serialized model artifact
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies

```


## 🚀 Quickstart Guide
1. Environment Setup
git clone [https://github.com/YOUR_USERNAME/fabric_defects_analysis.git](https://github.com/YOUR_USERNAME/fabric_defects_analysis.git)
cd fabric_defects_analysis
pip install -r requirements.txt

2. Execute the Data & AI Pipeline
Run the processing scripts in sequence to generate data, build Medallion layers, and train the model:

Step 1: Generate Raw Inspection Data (Bronze)
python src/genarate_data.py

Step 2: Run Data Transformations & Aggregations (Silver & Gold)
python src/pipeline.py

Step 3: Train Predictive Classification Model
python src/model.py

3. Launch Interactive Dashboard
streamlit run dashboard/app.py

## 📊 Dashboard Features
 * Executive Metrics Summary: Real-time visibility into total inspections, defect rate (%), overall defect count, and scrap financial loss ($).
 * Line Performance Matrix: Gold-layer aggregated view comparing yield performance across fabric types and assembly lines.
 * Defect Analytics: Categorical distribution charts tracking broken yarns, creases, stains, and holes.

 
## ⚙️ Tools & Technologies
 * Language: Python 3.x
 * Data Engineering & Analysis: Pandas, NumPy
 * Machine Learning: Scikit-Learn, XGBoost, Joblib
 * Business Intelligence UI: Streamlit
 * Cloud & Tools: Git, GitHub, GitHub Codespaces

