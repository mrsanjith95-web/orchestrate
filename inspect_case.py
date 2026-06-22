import pandas as pd

claims = pd.read_csv("data/claims.csv")

row = claims.iloc[0]

print("User ID:", row["user_id"])
print("Claim Object:", row["claim_object"])

print("\nClaim:")
print(row["user_claim"])

print("\nImages:")

for img in row["image_paths"].split(";"):
    print(img)