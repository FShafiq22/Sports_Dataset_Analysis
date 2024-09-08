import pandas as pd

df = pd.read_csv("pl-tables-1993-2024.csv")
pd.set_option("display.max_rows", 646)
# print(df)

# df.info()
# print(df.describe())
# print(df["gd"].value_counts())
# print(df.sort_values(by=["gd"], ascending=False))