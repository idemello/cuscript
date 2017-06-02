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

page = requests.get('https://www.creditunionsonline.com/credit-union-6644.html')
tree = html.fromstring(page.content)
address = tree.xpath('//span[@itemprop="streetAddress"]/text()')
city = tree.xpath('//span[@itemprop="addressLocality"]/text()')
state = tree.xpath('//span[@itemprop="addressRegion"]/text()')
zip = tree.xpath('//span[@itemprop="postalCode"]/text()')
phone = tree.xpath('//div[@class="textH"]/span/text()')

#print to console
	
print(address)
print(city)
print(state)
print(zip)
print(phone)

