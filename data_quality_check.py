import pandas as pd
import os

data_path = "data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(data_path, file))

        print("\n" + "="*60)
        print(f"FILE: {file}")

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())