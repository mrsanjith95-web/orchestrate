import pandas as pd

from agents.process_claim import process_claim

claims = pd.read_csv("data/claims.csv")

row = claims.iloc[0]

results = process_claim(row)

for r in results:
    print(r)