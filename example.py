# Open the file "example.txt" in read mode
f = open("example.txt", "r")

# Read the contents of the file
data = f.read()

# Close the file
f.close()

# Print the contents of the file
print(data)

# Open the file "test.txt" in read mode
f = open("test.txt", "r")

# Read all lines of the file into a list
lines = f.readlines()

# Print each line in the list
for line in lines:
    print(line)

# Read the next line from the file (this will return an empty string because the file pointer is at the end)
line = f.readline()
# Read and print lines in a loop until the end of the file
while line:
    print(line)
    line = f.readline()
# Close the file
f.close()

# Import the os.path module
import os.path

# Check if the file "test.txt" exists
if os.path.isfile("test.txt"):
    print("\nFile exists")
else:
    print("\nFile doesn't exist")

# Open the file "test.txt" in read mode
f = open("test.txt", "r")
# Read all lines of the file into a list
mylist = f.readlines()
# Close the file
f.close()

# Specify the filename
filename = "test.txt"

# Check if the file exists
if os.path.isfile(filename):
    # Open and read the contents of the file using a context manager
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)
else:
    print("File doesn't exist")

# Import the csv module
import csv

# Open the CSV file "game.csv" in read mode
with open("game.csv", newline="") as csvfile:
    # Create a CSV reader object with a comma delimiter
    reader = csv.reader(csvfile, delimiter=",")
    # Iterate through each row in the CSV file and print it
    for row in reader:
        print(row)
