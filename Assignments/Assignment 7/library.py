import sqlite3
conn = sqlite3.connect("library.db") # opens library.db, or creates it
cur = conn.cursor() # the cursor is used to execute SQL commands

# Remove the old table, so this step can be run again.
cur.execute("DROP TABLE IF EXISTS books")

#Create a table named books with its columns.
cur.execute("""
CREATE TABLE books
( id INT PRIMARY KEY,
title VARCHAR(30) NOT NULL,
author VARCHAR(30) NOT NULL,
year INT,
genre VARCHAR(20),
copies INT,
rating NULL)""")

#_____Add at least 8 books. Use at least 3 different genres____
#Added one book with a single INSERT statement.
cur.execute("INSERT INTO books VALUES (1, 'Pride and Prejudice', 'Jane Austen', 1813, 'romance', 5, 4)")

#add the rest of the books with a list of tuples and executemany using ? placeholders.
books = [
(2, "The Count of Monte Cristo", "Alexandre Dumas", 1944, "adventure", 3, None),
(3, "Jane Eyre", "Charlotte Brontë", 1947, "romance", 2, 4),
(4, "The three musketeers", "Alexandre Dumas", 1844, "adventure", 2, 4),
(5, "The prisoner of zenda", "Anthony Hope", 1894, "Fiction", 3, 3),
(6, "Treasure Island", "Robert Louis Stevenson", 1883, "adventure", 4, 3),
(7, "The last of the Mohicans", "James Fenimore Cooper", 1826, "Fiction", 2, None),
(8, "Wuthering Heights", "Emily Brontë", 1959, "romance", 2, 4),
]
cur.executemany("INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)", books)


# Print the title and author of books published after 1990.
print("\nThe titles and authors of books published after 1990 are:")
cur.execute("SELECT title, author FROM books WHERE year > 1990")
for row in cur.fetchall():
    print(row)

#Print the title of fiction books with more than 2 copies (AND).
print("\nThe titles of Fiction books with more than 2 copies are:")
cur.execute("SELECT title FROM books WHERE genre = 'Fiction' AND copies > 2")
for row in cur.fetchall():
    print(row)

#Print the title of books published before 1900 or rated 5 (OR)
print("\nThe titles of books published before 1900 or rated 5 are:")
cur.execute("SELECT title FROM books WHERE year < 1900 OR rating = 5")
for row in cur.fetchall():
    print(row)

# Print the title of books that are not in the Mystery genre (NOT).
print("\nThe titles of books that are not in the Mystery genre are:")
cur.execute("SELECT title FROM books WHERE NOT genre = 'Mystery'")
for row in cur.fetchall():
    print(row)

# Print the title of books in either the Science or History genre (IN).
print("\nThe titles of books in either the Science or History genres are:") 
cur.execute("SELECT title FROM books WHERE genre IN ('Science', 'History')")
for row in cur.fetchall():
    print(row)

#Ask the user for a letter, then print the authors whose names start with that letter (LIKE). Pass the letter with a ? placeholder.
letter = input("\nEnter a letter to search for authors: ").strip()

print(f"\nAuthors whose names start with '{letter}':")

cur.execute(
    "SELECT DISTINCT author FROM books WHERE author LIKE ?",
    (letter + "%",)
)

for row in cur.fetchall():
    print(row[0])

#Print the title of books that have no rating (IS NULL).
print("\nThe titles of books that have no rating are:")
cur.execute("SELECT title FROM books WHERE rating IS NULL")
for row in cur.fetchall():
    print(row)

# save the changes to the file
conn.commit() 
conn.close()
print("The library database has been created.")
