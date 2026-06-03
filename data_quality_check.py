import pandas as pd
import os

data_path = "data/raw"

csv_files = sorted(
    [f for f in os.listdir(data_path) if f.endswith(".csv")]
)

for file in csv_files:
    print("\n" + "="*70)
    print(file)
    print("="*70)

    df = pd.read_csv(os.path.join(data_path, file))

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())