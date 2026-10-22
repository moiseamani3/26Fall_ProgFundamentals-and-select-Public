import sqlite3

conn = sqlite3.connect("StudentRecords.db")
cur = conn.cursor()

# 1. Remove the existing table, then create it.
cur.execute("DROP TABLE IF EXISTS StudentRecords")

cur.execute("""
CREATE TABLE StudentRecords (
    ID INT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    Age INT,
    Major VARCHAR(20)
)
""")

# 2. Add five students with fixed values.
students = [
    (1, "Davin", 25, "History"),
    (2, "Isaac", 23, "Mathematics"),
    (3, "Bruno", 18, "Geography"),
    (4, "David", 22, "Computer Science"),
    (5, "Luthor", 20, "Computer Science")
]

cur.executemany(
    """
    INSERT INTO StudentRecords (ID, Name, Age, Major)
    VALUES (?, ?, ?, ?)
    """,
    students
)

# 3. Print each student's name, age, and major, but not ID.
print("\nAll students ordered by ID:")

cur.execute("""
SELECT Name, Age, Major
FROM StudentRecords
ORDER BY ID
""")

for name, age, major in cur.fetchall():
    print(f"Name: {name}, Age: {age}, Major: {major}")

# 4. Ask whether to add a new student.
while True:
    answer = input(
        "\nDo you want to add a new student? (yes/no) "
    ).strip().lower()

    if answer in ("yes", "no"):
        break

    print("Please enter yes or no.")

if answer == "yes":
    # 5. Get and validate the student's information.
    while True:
        name = input("Enter the student's name: ").strip()

        if name:
            break

        print("Name cannot be empty.")

    while True:
        age = input("Enter the student's age: ").strip()

        if age.isdecimal():
            age = int(age)
            break

        print("Please enter a whole number for the age.")

    while True:
        major = input("Enter the student's major: ").strip()

        if major:
            break

        print("Major cannot be empty.")

    # 6. Assign an unused ID and insert with ? placeholders.
    cur.execute("SELECT MAX(ID) FROM StudentRecords")
    new_id = cur.fetchone()[0] + 1

    cur.execute(
        """
        INSERT INTO StudentRecords (ID, Name, Age, Major)
        VALUES (?, ?, ?, ?)
        """,
        (new_id, name, age, major)
    )

    print("New student added.")

# 7. Save changes and close the connection.
conn.commit()

# Display the updated list, including the new student.
print("\nUpdated list of all students:")

cur.execute("""
SELECT Name, Age, Major
FROM StudentRecords
ORDER BY ID
""")
#sorting by IDs but no displyaying them.
for name, age, major in cur.fetchall():
    print(f"Name: {name}, Age: {age}, Major: {major}")

conn.close()