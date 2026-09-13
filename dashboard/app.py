import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Fabric Quality & AI Analytics", layout="wide"
)

st.title("🧵 Fabric Quality Defect & AI Analytics Dashboard")
st.markdown(
    "**End-to-End Enterprise Data & AI Pipeline** | Real-Time Inspection Monitoring"
)

# Load Aggregated Gold Data
try:
    gold_kpis = pd.read_csv("data/gold_kpis.csv")
    silver_data = pd.read_csv("data/silver_inspections.csv")

    # Top Metrics Bar
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Inspections", len(silver_data))
    col2.metric("Total Defective Batches", int(silver_data["is_defective"].sum()))
    col3.metric(
        "Avg Defect Rate",
        f"{(silver_data['is_defective'].mean() * 100):.1f}%",
    )
    col4.metric(
        "Total Scrap Cost ($)", f"${silver_data['scrap_cost_usd'].sum():,.2f}"
    )

    st.divider()

    # Layout: Data Tables & Charts
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Production Line Performance (Gold Layer)")
        st.dataframe(gold_kpis, use_container_width=True)

    with col_right:
        st.subheader("Defect Types Distribution")
        defect_counts = (
            silver_data[silver_data["defect_type"] != "None"]["defect_type"]
            .value_counts()
        )
        st.bar_chart(defect_counts)

except FileNotFoundError:
    st.error(
        "Data files not found. Please run pipeline scripts first!"
    )
