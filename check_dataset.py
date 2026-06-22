import pandas as pd

files = [
    "data/claims.csv",
    "data/sample_claims.csv",
    "data/user_history.csv",
    "data/evidence_requirements.csv"
]

for file in files:
    print("\n" + "=" * 60)
    print(file)

    df = pd.read_csv(file)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 3 Rows:")
    print(df.head(3))