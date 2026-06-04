import pandas as pd
from pathlib import Path

input_path = Path("data/raw/nav_history.csv")
output_path = Path("data/processed/02_nav_history_clean.csv")

df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# date conversion
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# sort
df = df.sort_values(["amfi_code", "date"])

# NAV numeric
df["nav"] = pd.to_numeric(df["nav"], errors="coerce")

# remove invalid NAV
df = df[df["nav"] > 0]

# forward fill NAV (per fund)
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# remove duplicates
df = df.drop_duplicates()

df.to_csv(output_path, index=False)

print("Cleaned shape:", df.shape)
print("Saved:", output_path)
