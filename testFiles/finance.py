#! python3

#cuinfo.py - Saves specific info about credit unions across Hawaii

#imports - I have no idea what to import
##import csv
##import webbrowser
##import requests
##import bs4
##from bs4 import BeautifulSoup
from lxml import html
import requests

#retrieve web page with our data, parse it using html module ad save results in tree

page = requests.get('https://www.creditunionsonline.com/credit-union-financials-6644.html')
tree = html.fromstring(page.content)

finance = tree.xpath('//div[@class="financeTable"]/div[@class="hoursRow"]/div[@class="hoursCell hoursR"]/text()')

assets = finance[2]
loans = finance[3]
netWorth = finance[4]
members = finance[5]
fullTime = finance[6]
partTime = finance[7]

print(assets)
print(loans)
print(netWorth)
print(members)
print(fullTime)
print(partTime)


