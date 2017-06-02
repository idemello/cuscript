#! python3

#cuinfo.py - Saves specific info about credit unions across Hawaii

#imports - I have no idea what to import
##import csv
##import webbrowser
##import requests
import bs4
from bs4 import BeautifulSoup
from lxml import html
import requests

#retrieve web page with our data, parse it using html module ad save results in tree

page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
tree = html.fromstring(page.content)

bname = tree.xpath('//div[@class="sR"]/a/text()')
link = tree.xpath('//div[@class="sR"]/a/@href')

for i in range(2):
	
	bname = tree.xpath('//div[@class="sR"]/a/text()')
	link = tree.xpath('//div[@class="sR"]/a/@href')

	print(bname[i] + "\n")
	link = tree.xpath('//div[@class="sR"]/a/@href')


	addressURL = 'http://www.creditunionsonline.com/'+ link[i]
	page = requests.get(addressURL)
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
	
	financeLinks = tree.xpath('//nav[@class="btnWrap"]/a/@href')
	financeURL = financeLinks[2]	
	page = requests.get(financeURL)
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

	page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
	tree = html.fromstring(page.content)	
