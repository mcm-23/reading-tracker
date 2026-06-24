import pandas as pd 
df = pd.read_csv("/Users/cy/Desktop/reading-tracker/reading_data.csv") # load the whole StoryGraph export into a table called df
                 
print(df.head()) # shows me a sneak peek of the what the file contains, prints the first 5 rows of the table
print(df.shape) # shows me the dimensions of the table, how many rows and columns
print(df.columns.tolist()) # to shows me the column names in a list, so I can see what data is available to me
print(df["Read Status"].value_counts()) #to shows me how many books are in each read status category, like "read" or "currently reading"

read_count = df[df["Read Status"] == "read"].shape[0] # counts how many books have been marked as "read" in the Read Status column, and store that number in a variable called read_count
print(f"You've actually finished {read_count} books.") # shows me how many books I've finished, using the read_count variable to fill iin the sentence "You've actually finished {read_count} books"

finished = df[df["Read Status"] == "read"] # filters the table to only include rows where the Read Status is "read", and store that filtered table in a variable called finished
average = finished["Star Rating"].mean() # sums and divides the Star Rating column of the finished table to calculate the average rating for all finished books, and store that average in a variable called average
print(f"Your average rating for finished books is {average}") # shows the average rating for finished books in the sentence "Your average rating for finished books is {average}"

five_stars = df[df["Star Rating"] == 5] # puts all the rows in the table where the Star Rating is 5, and store that filtered table in a variable called five_stars
print(f"You've given {len(five_stars)} books five stars.") # shows how many books I've given five stars to, using the len() function to count the number of rows in the five_stars table (+ place in the sentence)

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

print(df["Star Rating"].value_counts(dropna=False)) # shows the count of each unique value in the Star Rating column, including NaN values
unrated = df[(df["Read Status"] == "read") & (df["Star Rating"].isna())] # selects all the rows in the table where the Read Status is "read" and the Star Rating is NaN (not rated), and store that filtered table in a variable called unrated
print(f"You finished but never rated {len(unrated)} books.")
print(unrated["Title"])
unrated.to_csv("/Users/cy/Desktop/reading-tracker/books_to_rate.csv", index=False) # saves the unrated table to a new CSV file called "books_to_rate.csv" on my desktop, without including the index column in the output file

maas = df[df["Authors"].str.contains("Maas", na=False)] # filters the table to only include rows where the Authors column contains the string "Maas", and store that filtered table in a variable called maas
print(maas[["Title", "Read Status", "Star Rating"]])

dupes = df[df.duplicated(subset=["Title", "Authors"], keep=False)] # filters the table to only include rows that are duplicates based on the Title and Authors columns, and store that filtered table in a variable called dupes
print(f"{len(dupes)} rows are part of a duplicate set.")

df_sorted = df.sort_values("Star Rating", na_position="last") # sorts the table by the Star Rating column in ascending order, with NaN values placed at the end of the sorted table, and store that sorted table in a variable called df_sorted
df_clean = df_sorted.drop_duplicates(subset=["Title", "Authors"], keep="first") # removes duplicate rows from the df_sorted table based on the Title and Authors columns, keeping only the first occurrence of each duplicate set, and store that cleaned table in a variable called df_clean
print(f"Before: {len(df)} rows.  After cleaning: {len(df_clean)} rows.")

unrated_clean = df_clean[(df_clean["Read Status"] == "read") & (df_clean["Star Rating"].isna())] # filters the df_clean table to only include rows where the Read Status is "read" and the Star Rating is NaN (not rated), and store that filtered table in a variable called unrated_clean
print(f"Genuinely unrated finished books: {len(unrated_clean)}")
unrated_clean.to_csv("/Users/cy/Desktop/reading-tracker/books_to_rate.csv", index=False) # saves the unrated_clean table to a new CSV file called "books_to_rate.csv" on my desktop, without including the index column in the output file
