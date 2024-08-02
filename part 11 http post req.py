import requests

# URL for the JSONPlaceholder API endpoint
# that accepts POST requests
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Send a POST request to the API endpoint with the data
response = requests.post(url, json=data)

# Print the response text
print(response.text)
