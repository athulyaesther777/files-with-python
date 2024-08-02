# It's like extracting data from websites
# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://github.com/athulyaesther777"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")

# Print the title of the page
print(soup.title.string)

# Assuming 'product' is a class in the HTML, the following code extracts product details
products = soup.find_all("div", class_="product")

for product in products:
    name = product.find("div", class_="name").string
    price = product.find("div", class_="price").string
    print(name, price)
