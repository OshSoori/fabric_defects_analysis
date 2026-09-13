import pandas as pd


def run_pipeline():
    # 1. Read Raw Data (Bronze)
    df_raw = pd.read_csv("data/raw_inspection_logs.csv")

    # 2. Transform & Clean (Silver)
    df_silver = df_raw.dropna().copy()
    df_silver["timestamp"] = pd.to_datetime(df_silver["timestamp"])

    # 3. Create Aggregations (Gold - Business Metrics)
    gold_kpis = (
        df_silver.groupby(["line_id", "fabric_type"])
        .agg(
            total_inspections=("inspection_id", "count"),
            total_defects=("is_defective", "sum"),
            avg_gsm=("gsm", "mean"),
            total_scrap_cost=("scrap_cost_usd", "sum"),
        )
        .reset_index()
    )

    gold_kpis["defect_rate_pct"] = (
        gold_kpis["total_defects"] / gold_kpis["total_inspections"]
    ) * 100

    # Save processed outputs
    df_silver.to_csv("data/silver_inspections.csv", index=False)
    gold_kpis.to_csv("data/gold_kpis.csv", index=False)
    print("Pipeline executed: Silver and Gold datasets created successfully.")


if __name__ == "__main__":
    run_pipeline()
