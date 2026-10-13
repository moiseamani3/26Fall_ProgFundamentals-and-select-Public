import sqlite3

conn = sqlite3.connect("school.db") # opens school.db, or creates it
cur = conn.cursor() # the cursor runs SQL commands

# ---------- Create the table ----------
cur.execute("DROP TABLE IF EXISTS students")

cur.execute("""
CREATE TABLE students
( id INT NOT NULL,
name VARCHAR(30) NOT NULL,
age INT,
major VARCHAR(20),
credits INT,
email VARCHAR(40),
PRIMARY KEY (id) )
""")
print("Table created.")

# ---------- Add rows ----------
cur.execute("""
INSERT INTO students
VALUES (1, 'Maya', 18, 'Biology', 15, 'maya@example.edu')
""")

students = [
(2, "Leo", 21, "History", 45, None),
(3, "Ana", 19, "Biology", 30, "ana@example.edu"),
(4, "Sam", 22, "Math", 60, None),
(5, "Priya", 20, "Computer Science", 40, "priya@example.edu"),
(6, "Omar", 18, "Math", 12, "omar@example.edu"),
(7, "Mia", 23, "History", 75, "mia@example.edu"),
(8, "Jon", 19, "Computer Science", 28, None),
]
query = "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)"
cur.executemany(query, students)

conn.commit() # save the changes to the file
print("Students added.")

# ---------- Read rows ----------
print("\nEvery student:")
cur.execute("SELECT * FROM students")
rows = cur.fetchall()
for row in rows:
    print(row)

print("\nStudents aged 20 or older:")
cur.execute("SELECT name, age FROM students WHERE age >= 20")
for row in cur.fetchall():
    print(row)

major = "Biology"
print("\nStudents in", major)
cur.execute("SELECT name FROM students WHERE major = ?", (major,))
for row in cur.fetchall():
    print(row)

# ---------- Filter rows ----------
print("\nAND: Biology students under 19")
query = "SELECT name FROM students WHERE major = 'Biology' AND age < 19"
for row in cur.execute(query):
    print(row)
    
print("\nOR: Math students, or anyone with over 50 credits")
query = "SELECT name FROM students WHERE major = 'Math' OR credits > 50"
for row in cur.execute(query):
    print(row)
    
print("\nNOT: students not in History")
query = "SELECT name FROM students WHERE NOT major = 'History'"
for row in cur.execute(query):
    print(row)
print("\nIN: students in Biology or History")
query = "SELECT name FROM students WHERE major IN ('Biology', 'History')"
for row in cur.execute(query):
    print(row)
    
print("\nLIKE: names starting with M")
query = "SELECT name FROM students WHERE name LIKE 'M%'"
for row in cur.execute(query):
    print(row)
    
print("\nIS NULL: students with no email")
query = "SELECT name FROM students WHERE email IS NULL"
for row in cur.execute(query):
    print(row)



# ---------- Sort and summarize ----------
print("\nDISTINCT: each major once")
query = "SELECT DISTINCT major FROM students"
for row in cur.execute(query):
    print(row)
    
print("\nORDER BY: names from A to Z")
query = "SELECT name FROM students ORDER BY name"
for row in cur.execute(query):
    print(row)
    
print("\nORDER BY ... DESC: most credits first")
query = "SELECT name, credits FROM students ORDER BY credits DESC"
for row in cur.execute(query):
    print(row)


cur.execute("""
SELECT COUNT(*), SUM(credits), AVG(age), MIN(age), MAX(age)
FROM students
""")
count, total, average, youngest, oldest = cur.fetchone()
print("\nNumber of students:", count)
print("Total credits:", total)
print("Average age:", round(average, 1))
print("Youngest:", youngest, " Oldest:", oldest)
    

conn.close()
print("\nDone.")
