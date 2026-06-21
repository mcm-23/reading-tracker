# books.py my reading tracker, VO
import pandas as pd
df = pd.read_csv("/Users/cy/Desktop/storygraphdata.csv")

books = [
     {"title": "The Secret History", "pages": 559, "rating": 4.5, "genre": "dark academia"},
     {"title": "If We Were Villains", "pages": 354, "rating": 4.25, "genre": "dark academia"},
     {"title": "Frankenstein", "pages": 273, "rating": 4.0, "genre": "horror classic"},
     {"title": "Red White and Royal Blue", "pages": 440, "rating": 5, "genre": "comtemporary romance", "subgenre": "queer romance"},
     {"title": "The Song of Achilles", "pages": 378, "rating": 5, "genre": "historical fiction", "subgenre": "queer romance"},
     {"title": "Under One Roof", "pages": 112, "rating": 5, "genre": "contemporary romance"},
     {"title": "Jane Eyre", "pages": 652, "rating": 4.5, "genre": "classic romance", "subgenre": "gothic romance"},
     {"title": "Harry Potter and the Sorcerer's Stone", "pages": 320, "rating": 4.0, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Chamber of Secrets", "pages": 341, "rating": 4.0, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Prisoner of Azkaban", "pages": 435, "rating": 4.5, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Goblet of Fire", "pages": 734, "rating": 3.75, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Order of the Phoenix", "pages": 870, "rating": 4.0, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Half-Blood Prince", "pages": 652, "rating": 3.75, "genre": "fantasy", "subgenre": "young adult fantasy"},
     {"title": "Harry Potter and the Deathly Hallows", "pages": 759, "rating": 4.0, "genre": "fantasy", "subgenre": "young adult fantasy"},
]

print(f"You've logged {len(books)} books.")

total_pages = 0
for book in books:
    total_pages = total_pages + book["pages"]

print(f"That's {total_pages} pages total.")

genre_counts = {} # empty clipboard, no genre tallied yet

for book in books:
    genre = book["genre"] # grab this book's genre
    if genre in genre_counts: # have I seen this genre before?
        genre_counts[genre] += 1 # yes, add one to the count
    else:
        genre_counts[genre] = 1 # no, start the count at one
for genre, count in genre_counts.items():
    print(f"{genre}: {count}")

my_books = ["Iced", "Frankenstein", "Jane Eyre", "The Song of Achilles"]

# build len() by hand: count the items without using len()
count = 0
for book in my_books:
    count += 1        # every single pass, just bump it. no if needed.

print(f"There are {count} books.")
print(len(my_books))   # the real len(), to check your answer matches

unrated = df[(df["Read Status"] == "read") & (df["Star Rating"].isna())]
print(f"You finished but never rated {len(unrated)} books.")
print(unrated["Title"])
unrated.to_csv("/Users/cy/Desktop/books_to_rate.csv", index=False)