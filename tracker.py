import pandas as pd 
df = pd.read_csv("/Users/cy/Desktop/reading-tracker/storygraphdata.csv")  # load the whole StoryGraph export into a table called df

df_sorted = df.sort_values("Star Rating", na_position="last") # sorts the table by the Star Rating column in ascending order, with NaN values placed at the end of the sorted table, and store that sorted table in a variable called df_sorted
df_clean = df_sorted.drop_duplicates(subset=["Title", "Authors"], keep="first") # removes duplicate rows from the df_sorted table based on the Title and Authors columns, keeping only the first occurrence of each duplicate set, and store that cleaned table in a variable called df_clean
print(f"Before: {len(df)} rows.  After cleaning: {len(df_clean)} rows.")
                 
print(df_clean.head()) # shows me a sneak peek of the what the file contains, prints the first 5 rows of the table
print(df_clean.shape) # shows me the dimensions of the table, how many rows and columns
print(df_clean.columns.tolist()) # to shows me the column names in a list, so I can see what data is available to me
print(df_clean["Read Status"].value_counts()) #to shows me how many books are in each read status category, like "read" or "currently reading"

read_count = df_clean[df_clean["Read Status"] == "read"].shape[0] # counts how many books have been marked as "read" in the Read Status column, and store that number in a variable called read_count
print(f"You've actually finished {read_count} books.") # shows me how many books I've finished, using the read_count variable to fill iin the sentence "You've actually finished {read_count} books"

finished = df_clean[df_clean["Read Status"] == "read"] # filters the table to only include rows where the Read Status is "read", and store that filtered table in a variable called finished
average = finished["Star Rating"].mean() # sums and divides the Star Rating column of the finished table to calculate the average rating for all finished books, and store that average in a variable called average
print(f"Your average rating for finished books is {average}") # shows the average rating for finished books in the sentence "Your average rating for finished books is {average}"

print(df_clean["Star Rating"].value_counts(dropna=False)) # shows the count of each unique value in the Star Rating column, including NaN values

unrated_clean = df_clean[(df_clean["Read Status"] == "read") & (df_clean["Star Rating"].isna())] # filters the df_clean table to only include rows where the Read Status is "read" and the Star Rating is NaN (not rated), and store that filtered table in a variable called unrated_clean
print(f"Genuinely unrated finished books: {len(unrated_clean)}")
unrated_clean.to_csv("/Users/cy/Desktop/reading-tracker/books_to_rate.csv", index=False) # saves the unrated_clean table to a new CSV file called "books_to_rate.csv" on my desktop, without including the index column in the output file

tbr_count = df_clean[df_clean["Read Status"] == "to-read"].shape[0]
print(f"You have {tbr_count} books on your to-read pile.")

books_per_year = 60 
years_to_finish = tbr_count / books_per_year
print(f"At a rate of {books_per_year} books per year, it will take you {years_to_finish} years to finish your to-read pile.")
print(round(years_to_finish, 1)) # rounds the years_to_finish variable to one decimal place and prints it