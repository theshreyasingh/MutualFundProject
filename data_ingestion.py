import pandas as pd
import os

data_path = "data/raw"

csv_files = sorted(
    [f for f in os.listdir(data_path) if f.endswith(".csv")]
)

for file in csv_files:
    print("\n" + "=" * 70)
    print(f"FILE: {file}")
    print("=" * 70)

    try:
        df = pd.read_csv(os.path.join(data_path, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {file}: {e}")