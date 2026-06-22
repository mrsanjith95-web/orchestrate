import pandas as pd

sample = pd.read_csv("data/sample_claims.csv")

print("\nISSUE TYPES:")
print(sorted(sample["issue_type"].dropna().unique()))

print("\nOBJECT PARTS:")
print(sorted(sample["object_part"].dropna().unique()))

print("\nCLAIM STATUS:")
print(sorted(sample["claim_status"].dropna().unique()))

print("\nSEVERITY:")
print(sorted(sample["severity"].dropna().unique()))