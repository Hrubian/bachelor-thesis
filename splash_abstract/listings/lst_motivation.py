titanic = pd.read_csv("titanic.csv")
df = titanic # reference instead of copy
titanic.drop("Pclass", inplace=True)
byclass = df[["Pclass", "Survived"]]\
    .groupby("Pclass").mean() # Pclass undefined
byclass["Surviwed"] # <- typo