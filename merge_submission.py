import pandas as pd

files = [
    "output/submission_0_2.csv",
    "output/submission_2_5.csv",
    "output/submission_5_10.csv",
]

dfs = [pd.read_csv(f) for f in files]

# 10_15 but remove last overlapping row (user_025)
df_10_15 = pd.read_csv("output/submission_10_15.csv")
df_10_15 = df_10_15.iloc[:-1]
dfs.append(df_10_15)

# remaining files
for f in [
    "output/submission_14_20.csv",
    "output/submission_20_25.csv",
    "output/submission_25_30.csv",
    "output/submission_30_35.csv",
    "output/submission_35_40.csv",
    "output/submission_40_45.csv",
]:
    dfs.append(pd.read_csv(f))

final_df = pd.concat(dfs, ignore_index=True)

print("Rows:", len(final_df))

final_df.to_csv(
    "output/final_submission_fixed.csv",
    index=False
)

print("Saved output/final_submission_fixed.csv")