import pandas as pd
from agents.image_analyzer import analyze_image

# Load claims
claims = pd.read_csv("data/claims.csv")

# Take first claim
row = claims.iloc[0]

claim_text = row["user_claim"]

print("=" * 80)
print("USER ID:", row["user_id"])
print("CLAIM OBJECT:", row["claim_object"])
print("=" * 80)

print("\nCLAIM:")
print(claim_text)

print("\n" + "=" * 80)

# Split image paths
image_paths = row["image_paths"].split(";")

print(f"\nNumber of Images: {len(image_paths)}")

# Analyze each image
for index, image_path in enumerate(image_paths, start=1):

    print("\n" + "-" * 80)
    print(f"IMAGE {index}")
    print("PATH:", image_path)
    print("-" * 80)

    try:
        result = analyze_image(
            image_path,
            claim_text
        )

        print(result)

    except Exception as e:
        print("ERROR:", str(e))

print("\n" + "=" * 80)
print("CASE ANALYSIS COMPLETED")
print("=" * 80)