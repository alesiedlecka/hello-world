import requests
url = "http://www.floatrates.com/daily/usd.json"
resp = requests.get(url=url)  
data = resp.json()
from tabulate import tabulate
currencies = ["eur", "gbp"]
table = []
for currency in currencies:
	currency_data = data[currency]
	table.append([currency_data["name"],currency_data["rate"]])
print(tabulate(table))
	

