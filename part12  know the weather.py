import requests

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
url = "https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY"

# Send a GET request to the API endpoint
response = requests.get(url)

# Parse the response JSON
data = response.json()

# Extract temperature and humidity from the JSON data
temperature = data["main"]["temp"]  # Corrected "mian" to "main"
humidity = data["main"]["humidity"]

# Print the extracted temperature and humidity
print("Temperature:", temperature)
print("Humidity:", humidity)
