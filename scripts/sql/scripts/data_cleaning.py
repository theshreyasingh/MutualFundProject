import pandas as pd
from pathlib import Path

processed = Path("data/processed")

# ---------------------------
# NAV CLEANING
# ---------------------------
nav = pd.read_csv("data/raw/nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"], errors="coerce")
nav["nav"] = pd.to_numeric(nav["nav"], errors="coerce")

nav = nav.sort_values(["amfi_code", "date"])
nav = nav[nav["nav"] > 0]
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()
nav = nav.drop_duplicates()

nav.to_csv(processed / "02_nav_history_clean.csv", index=False)
print("NAV cleaned")

# ---------------------------
# TRANSACTIONS CLEANING
# ---------------------------
txn = pd.read_csv("data/raw/investor_transactions.csv")

txn["transaction_type"] = txn["transaction_type"].str.upper().str.strip()
txn["amount"] = pd.to_numeric(txn["amount"], errors="coerce")
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"], errors="coerce")

txn = txn[txn["amount"] > 0]
txn = txn.drop_duplicates()

txn.to_csv(processed / "08_investor_transactions_clean.csv", index=False)
print("Transactions cleaned")

# ---------------------------
# SCHEME PERFORMANCE CLEANING
# ---------------------------
perf = pd.read_csv("data/raw/scheme_performance.csv")

num_cols = ["1Y_return", "3Y_return", "5Y_return", "expense_ratio"]

for col in num_cols:
    if col in perf.columns:
        perf[col] = pd.to_numeric(perf[col], errors="coerce")

perf = perf.drop_duplicates()
perf = perf.dropna()

perf.to_csv(processed / "07_scheme_performance_clean.csv", index=False)
print("Performance cleaned")

print("ALL CLEANING DONE ✔")