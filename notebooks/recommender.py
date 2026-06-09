import pandas as pd

fund = pd.read_csv("../data/processed/01_fund_master_clean.csv")
sharpe = pd.read_csv("sharpe_results.csv")

df = fund.merge(
    sharpe,
    on="amfi_code"
)

risk = input(
    "Enter Risk Appetite (Low/Moderate/High): "
)

result = (
    df[df['risk_category'] == risk]
    .sort_values(
        'sharpe_ratio',
        ascending=False
    )
    .head(3)
)

print("\nTop Recommended Funds:\n")

print(
    result[
        [
            'scheme_name',
            'risk_category',
            'sharpe_ratio'
        ]
    ]
)
