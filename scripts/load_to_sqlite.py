import pandas as pd
from sqlalchemy import create_engine
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "bluestock_mf.db")

engine = create_engine(f"sqlite:///{db_path}")

def load(file, table):
    path = os.path.join(BASE_DIR, "data/processed", file)
    
    df = pd.read_csv(path)
    print(f"Loaded {file} -> {df.shape}")

    df.to_sql(table, engine, if_exists="replace", index=False)
    print(f"✔ Inserted into {table}")

load("02_nav_history_clean.csv", "fact_nav")
load("08_investor_transactions_clean.csv", "fact_transactions")
load("07_scheme_performance_clean.csv", "fact_performance")
load("03_aum_by_fund_house_clean.csv", "fact_aum")

print("✅ DATABASE READY")
print("DB LOCATION:", db_path)