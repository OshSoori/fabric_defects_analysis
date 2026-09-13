import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

n_samples = 1000

# Generate synthetic manufacturing metrics
data = {
    "inspection_id": [f"INS-{1000 + i}" for i in range(n_samples)],
    "timestamp": pd.date_range(
        start="2026-09-01", periods=n_samples, freq="15min"
    ),
    "batch_id": np.random.choice(
        ["BATCH-A", "BATCH-B", "BATCH-C", "BATCH-D"], size=n_samples
    ),
    "line_id": np.random.choice(["Line-1", "Line-2", "Line-3"], size=n_samples),
    "fabric_type": np.random.choice(
        ["Cotton", "Polyester Blend", "Linen", "Denim"], size=n_samples
    ),
    "gsm": np.random.normal(loc=180, scale=15, size=n_samples).round(1),
    "tensile_strength": np.random.normal(loc=45, scale=5, size=n_samples).round(
        2
    ),
    "defect_count": np.random.poisson(lam=1.5, size=n_samples),
    "defect_type": np.random.choice(
        ["None", "Broken Yarn", "Stain", "Hole", "Crease"],
        size=n_samples,
        p=[0.6, 0.15, 0.1, 0.05, 0.1],
    ),
}

df = pd.DataFrame(data)

# Derive business rules
df["is_defective"] = (df["defect_type"] != "None").astype(int)
df["scrap_cost_usd"] = df["defect_count"] * np.random.choice(
    [12.5, 25.0, 40.0], size=n_samples
)

# Save raw dataset (Bronze Layer)
df.to_csv("data/raw_inspection_logs.csv", index=False)
print("Successfully generated data/raw_inspection_logs.csv with 1,000 records.")
import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

n_samples = 1000

# Generate synthetic manufacturing metrics
data = {
    "inspection_id": [f"INS-{1000 + i}" for i in range(n_samples)],
    "timestamp": pd.date_range(
        start="2026-09-01", periods=n_samples, freq="15min"
    ),
    "batch_id": np.random.choice(
        ["BATCH-A", "BATCH-B", "BATCH-C", "BATCH-D"], size=n_samples
    ),
    "line_id": np.random.choice(["Line-1", "Line-2", "Line-3"], size=n_samples),
    "fabric_type": np.random.choice(
        ["Cotton", "Polyester Blend", "Linen", "Denim"], size=n_samples
    ),
    "gsm": np.random.normal(loc=180, scale=15, size=n_samples).round(1),
    "tensile_strength": np.random.normal(loc=45, scale=5, size=n_samples).round(
        2
    ),
    "defect_count": np.random.poisson(lam=1.5, size=n_samples),
    "defect_type": np.random.choice(
        ["None", "Broken Yarn", "Stain", "Hole", "Crease"],
        size=n_samples,
        p=[0.6, 0.15, 0.1, 0.05, 0.1],
    ),
}

df = pd.DataFrame(data)

# Derive business rules
df["is_defective"] = (df["defect_type"] != "None").astype(int)
df["scrap_cost_usd"] = df["defect_count"] * np.random.choice(
    [12.5, 25.0, 40.0], size=n_samples
)

# Save raw dataset (Bronze Layer)
df.to_csv("data/raw_inspection_logs.csv", index=False)
print("Successfully generated data/raw_inspection_logs.csv with 1,000 records.")
