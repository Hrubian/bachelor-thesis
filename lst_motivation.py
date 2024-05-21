import pandas as pd

df = pd.read_csv("data.csv")
df_copy = df
df_copy.drop("column1", inplace=True)

grouped = df.groupby("column1")
# Error - column1 does not exist already

final_score = df["score_a"] + df["score_b_note"]
# Error - summing Series of ints with strings

print(df["colunm2"])
# Error - misspelled column name colunm2
