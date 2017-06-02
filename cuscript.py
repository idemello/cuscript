#Authors: Isaac DeMello, Jie Zhou, Wendy Chong
#cuinfo.py - Saves specific info about credit unions across Hawaii

from lxml import html
import requests

#using the requests module go to the initial page
#convert the content of the page into a tree using the lxml libary
#addressLinks generates a list of links to go from the first page to the second page

page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
tree = html.fromstring(page.content)
addressLink = tree.xpath('//div[@class="sR"]/a/@href')

print(financeLinks)
for i in range(10):

#get the initial name of the bank
#generate a list of links
	
	bname = tree.xpath('//div[@class="sR"]/a/text()')

#Print the name of the bank for the current iteration#

	print(bname[i])

#concatenate the base URL with the current iteration to traverse to the next page
#using the generated url to get to the next page
#get the necessary address information using lxml


	addressURL = 'http://www.creditunionsonline.com/'+ addressLink[i]
	page = requests.get(addressURL)
	tree = html.fromstring(page.content)
	address = tree.xpath('//span[@itemprop="streetAddress"]/text()')
	city = tree.xpath('//span[@itemprop="addressLocality"]/text()')
	state = tree.xpath('//span[@itemprop="addressRegion"]/text()')
	zip = tree.xpath('//span[@itemprop="postalCode"]/text()')
	phone = tree.xpath('//div[@class="textH"]/span/text()')

#print address information 
	
	print(address)
	print(city)
	print(state)
	print(zip)
	print(phone)

#generate a new new url based on the financeLinks list
#use the generated url to go to the next page
#generate an html tree structure
	
	financeLinks = tree.xpath('//nav[@class="btnWrap"]/a/@href')	
	financeURL = financeLinks[-1]	
	page = requests.get(financeURL)
	tree = html.fromstring(page.content)

#create a list of all financial information

	finance = tree.xpath('//div[@class="financeTable"]/div[@class="hoursRow"]/div[@class="hoursCell hoursR"]/text()')

#parse the finance list for necessary data

	assets = finance[2]
	loans = finance[3]
	netWorth = finance[4]
	members = finance[5]
	fullTime = finance[6]
	partTime = finance[7]

#print finance data

	print(assets)
	print(loans)
	print(netWorth)
	print(members)
	print(fullTime)
	print(partTime)		

#go back to the initial page

	page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
	tree = html.fromstring(page.content)	
