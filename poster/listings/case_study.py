import pandas as pd

attendees_df = pd.read_csv("attendees.csv")
matches_df = pd.read_csv("matches.csv") \
    .rename(columns={"name": "match_name"})
scores_df = pd.read_csv("scores.csv")

attendees_df["name_surname"] = \
    attendees_df["name"] + "_" + attendees_df["surname"]
attendees_df = attendees_df.drop(columns=["name", "surname"])

scores_with_match_name_df = scores_df \
    .merge(matches_df, left_on="match_id", right_on="id") \
    .drop(columns="id")

scores_with_age_df = pd.merge(
    scores_with_match_name_df, attendees_df, on="name_surname"
)

top_two_per_age_df = scores_with_age_df \
    .sort_values("age") \
    .groupby(["age", "match_name"]) \
    .head(2) \
    .drop(columns=["match_id"])

top_two_per_age_df.to_csv("top_two_per_age.csv")
