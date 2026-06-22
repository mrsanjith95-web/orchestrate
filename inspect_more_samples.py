import pandas as pd

sample = pd.read_csv("data/sample_claims.csv")

print(sample[[
    "issue_type",
    "object_part",
    "claim_status",
    "supporting_image_ids"
]].head(15))