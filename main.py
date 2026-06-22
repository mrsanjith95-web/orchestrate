import pandas as pd

from agents.process_claim import process_claim
from agents.multi_image_decision import combine_results

# ----------------------------------
# CHANGE THESE FOR EACH BATCH
# ----------------------------------

START = 5
END = 10
# Batch 1 -> 0,5
# Batch 2 -> 5,10
# Batch 3 -> 10,15
# Batch 4 -> 15,20
# Batch 5 -> 20,25
# etc.

# ----------------------------------

claims = pd.read_csv("data/claims.csv")

output_rows = []

batch_claims = claims.iloc[START:END]

for index, row in batch_claims.iterrows():

    print(f"\nProcessing Claim {index + 1}")

    try:

        image_results = process_claim(row)

        if len(image_results) == 0:

            output_rows.append({
                "user_id": row["user_id"],
                "image_paths": row["image_paths"],
                "user_claim": row["user_claim"],
                "claim_object": row["claim_object"],
                "issue_type": "unknown",
                "object_part": "unknown",
                "claim_status": "not_enough_information",
                "severity": "unknown",
                "supporting_image_ids": "none"
            })

            continue

        final = combine_results(image_results)

        output_rows.append({

            "user_id": row["user_id"],
            "image_paths": row["image_paths"],
            "user_claim": row["user_claim"],
            "claim_object": row["claim_object"],

            "issue_type": final["issue_type"],
            "object_part": final["object_part"],
            "claim_status": final["claim_status"],
            "severity": final["severity"],
            "supporting_image_ids": final["supporting_image_ids"]

        })

    except Exception as e:

        print("ERROR:", e)

        output_rows.append({
            "user_id": row["user_id"],
            "image_paths": row["image_paths"],
            "user_claim": row["user_claim"],
            "claim_object": row["claim_object"],
            "issue_type": "unknown",
            "object_part": "unknown",
            "claim_status": "not_enough_information",
            "severity": "unknown",
            "supporting_image_ids": "none"
        })

# ----------------------------------
# Full Output
# ----------------------------------

df = pd.DataFrame(output_rows)

output_file = f"output/output_{START}_{END}.csv"

df.to_csv(
    output_file,
    index=False
)

# ----------------------------------
# Submission Output
# ----------------------------------

submission_df = df[
    [
        "user_id",
        "issue_type",
        "object_part",
        "claim_status",
        "severity",
        "supporting_image_ids"
    ]
]

submission_file = f"output/submission_{START}_{END}.csv"

submission_df.to_csv(
    submission_file,
    index=False
)

print("\nDone.")
print(f"Saved full output to {output_file}")
print(f"Saved submission file to {submission_file}")