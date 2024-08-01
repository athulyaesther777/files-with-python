
import json

data = '''

[
    {
        "id" : 1,
         "name" : "Robert Amil",
         "age" : 27,
        "Strength": [
            "Programming",
            "Leadership",
            "Logical Thinking"

        ]
    }
]

'''

# Parse the JSON data
parsed_data = json.loads(data)

# Access and print the data
for person in parsed_data:
    print(f"ID: {person['id']}")
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print("Strengths: ", ", ".join(person['Strength']))
