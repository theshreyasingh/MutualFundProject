from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

processed = Path("data/processed")

for file in processed.glob("*.csv"):
    df = pd.read_csv(file)

    table_name = file.stem

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {table_name}")