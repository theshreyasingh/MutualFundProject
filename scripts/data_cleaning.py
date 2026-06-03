from pathlib import Path
import pandas as pd

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

PROCESSED.mkdir(exist_ok=True)

# ------------------------
# NAV HISTORY
# ------------------------

nav = pd.read_csv(RAW / "02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav.to_csv(PROCESSED / "02_nav_history_clean.csv", index=False)

print("NAV cleaned")

# ------------------------
# INVESTOR TRANSACTIONS
# ------------------------

txn = pd.read_csv(RAW / "08_investor_transactions.csv")

txn["transaction_date"] = pd.to_datetime(txn["transaction_date"])

txn["transaction_type"] = (
    txn["transaction_type"]
    .str.strip()
    .str.title()
)

txn = txn[txn["amount_inr"] > 0]

valid_kyc = ["Verified", "Pending"]

txn = txn[txn["kyc_status"].isin(valid_kyc)]

txn.to_csv(
    PROCESSED / "08_investor_transactions_clean.csv",
    index=False
)

print("Transactions cleaned")

# ------------------------
# SCHEME PERFORMANCE
# ------------------------

perf = pd.read_csv(RAW / "07_scheme_performance.csv")

perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

perf.to_csv(
    PROCESSED / "07_scheme_performance_clean.csv",
    index=False
)

print("Performance cleaned")
# Copy remaining datasets to processed folder

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in remaining_files:
    df = pd.read_csv(RAW / file)

    output_name = file.replace(".csv", "_clean.csv")

    df.to_csv(PROCESSED / output_name, index=False)

    print(f"Saved {output_name}")