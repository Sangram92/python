# Get product data from flipcart site using web scraping

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = "https://www.flipkart.com/"

# open CSV file to write the data
filename = "product.csv"
f = open(filename, "w", encoding="utf-8")
headers = "Name, Offer or Price, Description\n"
f.write(headers)

# opening up connect & grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")
products = page_soup.findAll("div", {"class": "_2kSfQ4"})


product_list = []

# iterate on product and extract name, price & description
for product in products:
	product_name = product.findAll("div", {"class": "iUmrbN"})[0].text
	offer_or_price = product.findAll("div", {"class": "BXlZdc"})[0].text
	description = product.findAll("div", {"class": "_3o3r66"})[0].text
    
	product_list.append({
		"name": product_name,
		"offer_or_price": offer_or_price,
		"description": description
	})

	f.write(product_name.replace(",", "|")
		+ "," + offer_or_price.replace(",", "|")
		+ "," + description.replace(",", "|") + "\n")

f.close()