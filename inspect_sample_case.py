import pandas as pd

sample = pd.read_csv("data/sample_claims.csv")

for i in range(5):
    print("\n" + "="*80)
    print(sample.iloc[i][[
        "claim_object",
        "issue_type",
        "object_part",
        "claim_status",
        "severity",
        "supporting_image_ids"
    ]])