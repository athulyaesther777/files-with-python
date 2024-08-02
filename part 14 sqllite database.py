import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'students' with columns 'name' and 'age'
cursor.execute("CREATE TABLE IF NOT EXISTS students (name TEXT, age INTEGER)")

# Insert a record into the 'students' table
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Annies", 16))


# Insert a record into the 'students' table
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Esther", 10))

# Commit the changes to the database
conn.commit()

# Query all records from the 'students' table
cursor.execute("SELECT * FROM students")

# Fetch all results from the executed query
results = cursor.fetchall()

# Print the fetched results
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
