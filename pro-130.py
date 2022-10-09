import csv
import pandas as pd

df = pd.read_csv("total_stars.csv")
print(df.shape)
del df["luminosity"]
del df["star_name"]
del df["distance"]
del df["mass"]
del df["radius"]

print(df.shape)
df.to_csv("cleaned_stars.csv")