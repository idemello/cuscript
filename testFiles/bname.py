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

page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
tree = html.fromstring(page.content)

bname = tree.xpath('//div[@class="sR"]/a/text()')

for i in range(61):
	print(bname[i] + "\n")
