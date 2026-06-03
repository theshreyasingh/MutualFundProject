import pandas as pd

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing = master_codes - nav_codes

print("Fund Master Codes:", len(master_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing))

if len(missing) == 0:
    print("PASS: All AMFI codes exist in NAV history")
else:
    print("Missing Codes:")
    print(missing)