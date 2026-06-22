import pandas as pd

claims = pd.read_csv("data/claims.csv")

row = claims.iloc[0]

images = row["image_paths"].split(";")

print("Number of Images:", len(images))

for img in images:
    print(img)