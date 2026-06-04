import pandas as pd
from pathlib import Path

input_path = Path("data/raw/scheme_performance.csv")
output_path = Path("data/processed/07_scheme_performance_clean.csv")

df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# -------------------------
# numeric conversion
# -------------------------
num_cols = ["1Y_return", "3Y_return", "5Y_return", "expense_ratio"]

for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# -------------------------
# remove invalid returns
# -------------------------
df = df.dropna(subset=["1Y_return", "3Y_return", "5Y_return"])

# -------------------------
# expense ratio filter
# -------------------------
if "expense_ratio" in df.columns:
    df = df[(df["expense_ratio"] >= 0.1) & (df["expense_ratio"] <= 2.5)]

# -------------------------
# remove duplicates
# -------------------------
df = df.drop_duplicates()

df.to_csv(output_path, index=False)

print("Cleaned shape:", df.shape)
print("Saved:", output_path)