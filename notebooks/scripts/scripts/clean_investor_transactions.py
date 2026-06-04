import pandas as pd
from pathlib import Path

# paths
input_path = Path("data/raw/investor_transactions.csv")
output_path = Path("data/processed/08_investor_transactions_clean.csv")

# load data
df = pd.read_csv(input_path)

print("Original shape:", df.shape)

# -------------------------
# 1. Standardize transaction_type
# -------------------------
df["transaction_type"] = df["transaction_type"].str.upper().str.strip()

valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]
df = df[df["transaction_type"].isin(valid_types)]

# -------------------------
# 2. Fix amount
# -------------------------
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df = df[df["amount"] > 0]

# -------------------------
# 3. Fix date format
# -------------------------
df["transaction_date"] = pd.to_datetime(df["transaction_date"], errors="coerce")
df = df.dropna(subset=["transaction_date"])

# -------------------------
# 4. KYC validation (basic)
# -------------------------
if "kyc_status" in df.columns:
    df["kyc_status"] = df["kyc_status"].str.upper().str.strip()
    valid_kyc = ["VERIFIED", "PENDING", "REJECTED"]
    df = df[df["kyc_status"].isin(valid_kyc)]

# -------------------------
# 5. Remove duplicates
# -------------------------
df = df.drop_duplicates()

# -------------------------
# save
# -------------------------
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print("Cleaned shape:", df.shape)
print("Saved:", output_path)