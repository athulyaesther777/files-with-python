import json

# Define your JSON data as a string
json_data = '''
[
    {"name": "Item 1", "description": "Description of Item 1"},
    {"name": "Item 2", "description": "Description of Item 2"},
    {"name": "Item 3", "description": "Description of Item 3"}
]
'''

# Parse the JSON data
data = json.loads(json_data)

# Iterate through the list and print each item's name and description
for item in data:
    print(item["name"])
    print(item["description"])
