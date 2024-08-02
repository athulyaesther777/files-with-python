import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'peoplelist' with columns 'id', 'name', and 'email'
cursor.execute("""
CREATE TABLE IF NOT EXISTS peoplelist(
id INTEGER PRIMARY KEY,
name TEXT,
email TEXT 
);
""")

# Insert a record into the 'peoplelist' table
cursor.execute("""
INSERT INTO peoplelist (id, name, email)
VALUES (1, "MILK", "milk333@gmail.com");
""")

# Insert another record into the 'peoplelist' table (correcting table name)
cursor.execute("""
INSERT INTO peoplelist (id, name, email)
VALUES (2, "MOCHA", "mocha777@gmail.com");
""")

# Commit the changes to the database
conn.commit()

# Fetch all records from the 'peoplelist' table
cursor.execute("""
SELECT * FROM peoplelist;
""")
results = cursor.fetchall()
print("All records:")
for row in results:
    print(row)

# Fetch name and email from the 'peoplelist' table
cursor.execute("""
SELECT name, email FROM peoplelist;
""")
results = cursor.fetchall()
print("\nName and email:")
for row in results:
    print(row)

# Fetch records where id is 1
cursor.execute("""
SELECT * FROM peoplelist
WHERE id = 1;
""")
results = cursor.fetchall()
print("\nRecord with id=1:")
for row in results:
    print(row)

# Fetch all records from the 'peoplelist' table ordered by name
cursor.execute("""
SELECT * FROM peoplelist
ORDER BY name;
""")
results = cursor.fetchall()
print("\nAll records ordered by name:")
for row in results:
    print(row)

# Fetch limited records from the 'peoplelist' table (LIMIT 2)
cursor.execute("""
SELECT * FROM peoplelist
LIMIT 2;
""")
results = cursor.fetchall()
print("\nLimited records (2):")
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
conn.close()
