import pandas as pd 
df = pd.read_csv("/Users/cy/Desktop/storygraphdata.csv")
                 
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df["Read Status"].value_counts())

read_count = df[df["Read Status"] == "read"].shape[0]
print(f"You've actually finished {read_count} books.")

finished = df[df["Read Status"] == "read"]
average = finished["Star Rating"].mean()
print(f"Your average rating for finished books is {average}")

five_stars = df[df["Star Rating"] == 5]
print(f"You've given {len(five_stars)} books five stars.")

three_stars = df[df["Star Rating"] == 3]
print(f"You've given {len(three_stars)} books three stars.")

two_stars = df[df["Star Rating"] == 2]
print(f"You've given {len(two_stars)} books two stars.")

one_stars = df[df["Star Rating"] == 1]
print(f"You've given {len(one_stars)} books one star.")

four_and_a_half_stars = df[df["Star Rating"] == 4.5]
print(f"You've given {len(four_and_a_half_stars)} books four and a half stars.")

four_stars = df[df["Star Rating"] == 4]
print(f"You've given {len(four_stars)} books four stars.")

print(df["Star Rating"].value_counts(dropna=False))
unrated = df[(df["Read Status"] == "read") & (df["Star Rating"].isna())]
print(f"You finished but never rated {len(unrated)} books.")
print(unrated["Title"])
unrated.to_csv("/Users/cy/Desktop/books_to_rate.csv", index=False)

maas = df[df["Authors"].str.contains("Maas", na=False)]
print(maas[["Title", "Read Status", "Star Rating"]])

dupes = df[df.duplicated(subset=["Title", "Authors"], keep=False)]
print(f"{len(dupes)} rows are part of a duplicate set.")

df_sorted = df.sort_values("Star Rating", na_position="last")
df_clean = df_sorted.drop_duplicates(subset=["Title", "Authors"], keep="first")
print(f"Before: {len(df)} rows.  After cleaning: {len(df_clean)} rows.")

unrated_clean = df_clean[(df_clean["Read Status"] == "read") & (df_clean["Star Rating"].isna())]
print(f"Genuinely unrated finished books: {len(unrated_clean)}")
unrated_clean.to_csv("/Users/cy/Desktop/books_to_rate.csv")
