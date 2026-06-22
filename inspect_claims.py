import pandas as pd

claims = pd.read_csv("data/claims.csv")

print("First Claim:")
print(claims.iloc[0])

print("\n" + "=" * 60 + "\n")

print("Second Claim:")
print(claims.iloc[1])