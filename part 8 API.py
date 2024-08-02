# Application Programming Interface API
"""
Whats is an API ?
its a set of instructions that computer can use to do things
eg ordering a dress in meesho , the website you use would sent instructions
to the meesho using a API
Most of the popular apps use APIs and we can use python to interact with it .
like LinkedIn , Spotify , Amazon and so on

"""
#pip install requests

import requests

# URL of the web page you want to fetch
#Imports the requests library,
# which is used for making HTTP requests in Python.

url = "https://github.com/athulyaesther777"

# Send an HTTP GET request to the specified URL
response = requests.get(url)

# Print the text content of the response
print(response.text)

