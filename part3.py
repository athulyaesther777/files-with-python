import json  # Import the json module to work with JSON data

# Open the JSON file in read mode
# The "with open" statement ensures that the file is properly closed after reading
with open("data.json", "r") as f:
    # Load the contents of the file into a Python dictionary using json.load()
    # This reads the JSON file and converts it into a Python dictionary
    data = json.load(f)

    # Print the data
    # This prints the Python dictionary representation of the JSON data
    print(data)
