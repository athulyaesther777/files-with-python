import requests

# Define your API key and city
api_key = "YOUR_API_KEY"  # Replace with your actual OpenWeatherMap API key
city = "London"

# Construct the URL with the API key and city
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Send a GET request to the API endpoint
response = requests.get(url)

# Parse the response JSON
data = response.json()

# Print the temperature from the JSON data
print("Temperature:", data["main"]["temp"])
