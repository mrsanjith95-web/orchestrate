import pandas as pd

sample = pd.read_csv("data/sample_claims.csv")

print("\nCLAIM STATUS")
print(sample["claim_status"].value_counts())

print("\nISSUE TYPE")
print(sample["issue_type"].value_counts())

print("\nOBJECT PART")
print(sample["object_part"].value_counts())