#! python3
# cuinfo.py - Saves specific info about credit unions across Hawaii

#imports - I have no idea what to import
import csv
import webbrowser
import requests
import bs4
from bs4 import BeautifulSoup


#starting url

url = 'https://www.creditunionsonline.com/hawaii-credit-unions.html'

#using BeautifulSoup4 module create a beautiful soup object of all pages

res = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')

#check if request was successful
#if request code is 200 == success
#elif 400< == failure 

res.raise_for_status() 
print(res.status_code)

cuinfo = bs4.BeautifulSoup(res.text)
print(type(cuinfo))
print(cuinfo)


