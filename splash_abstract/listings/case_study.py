# name:string, surname:string, age:int
atts_df = pd.read_csv("attendees.csv")
# id:int, name:string
matches_df = pd.read_csv("matches.csv") \
    .rename(columns={"name": "match_name"})
# name_surname:string, match_id:int, score:int
scores_df = pd.read_csv("scores.csv")

atts_df["name_surname"] = \
    atts_df["name"] + "_" + atts_df["surname"]
atts_df = atts_df.drop(columns=["name", "surname"])

scores_matches_df = scores_df \
    .merge(matches_df, left_on="match_id",
           right_on="id") \
    .drop(columns="id")

scores_with_age_df = pd.merge(
    scores_matches_df, atts_df, on="name_surname"
)
top_two_per_age_df = scores_with_age_df \
    .sort_values("age") \
    .groupby(["age", "match_name"]) \
    .head(2) \
    .drop(columns=["match_id"])
top_two_per_age_df.to_csv("top_two_per_age.csv")