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


#city = tree.xpath('//span[@itemprop="addressLocality"]/text()')
#state = tree.xpath('//span[@itemprop="addressRegion"]/text()')
#zip = tree.xpath('//span[@itemprop="postalCode"]/text()')
#phone = tree.xpath('//div[@class="textH"]/span/text()')

#print to console

#print(address)
#print(city)
#print(state)
#print(zip)
#print(phone)


#tree now contains the whole HTML file in a nice tree structure
#<span class="item-price">$29.95</span>
#prices = tree.xpath('//span[@class="item-price"]/text()')
#starting url
##url = 'https://www.creditunionsonline.com/hawaii-credit-unions.html'
#using BeautifulSoup4 module create a beautiful soup object of all pages
##res = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
#check if request was successful
#if request code is 200 == success
#elif 400< == failure
##res.raise_for_status()
##print(res.status_code)
##cuinfo = bs4.BeautifulSoup(res.text)
##print(cuinfo.select('div.sR a'))
###<meta name ="title: contect="McBryde Federal Credit Union - Eleele, HI">
