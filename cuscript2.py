#!/usr/bin/python3


#Authors: Isaac DeMello, Jie Zhou, Wendy Chong
#cuinfo.py - Saves specific info about credit unions across Hawaii

from lxml import html
import requests
import csv


def islandFind(zipCode):

    island = ""
    zipCode = zipCode[0]

    if  zipCode == '96705' or zipCode == '96752' or zipCode == '96766':
        island = "Kauai"
    elif zipCode == '96858' or zipCode == '96761' or zipCode == '96793':
        island = "Maui"
    elif zipCode == '96720' or zipCode == '96732' or zipCode == '96740' or zipCode == '96743' or zipCode == '96781' or zipCode == '96783':
        island = "Big Island"
    elif zipCode == '96748':
        island = "Molokai"
    else:
        island = "Oahu"
    
    return island

#using the requests module go to the initial page
#convert the content of the page into a tree using the lxml libary
#addressLinks generates a list of links to go from the first page to the second page

page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
tree = html.fromstring(page.content)
addressLink = tree.xpath('//div[@class="sR"]/a/@href')


addressList = []
cityList= []
stateList= []
zipcList = []
islandList = []
phoneList = []
branchList = []
assetsList = []
loansList = []
netWorthList = []
membersList = []
fullTimeList = []
partTimeList = []

for i in range(5):

#get the initial name of the bank
#generate a list of links
	
    bNameList = tree.xpath('//div[@class="sR"]/a/text()')

#Print the name of the bank for the current iteration#

	#print(bname[i])

#concatenate the base URL with the current iteration to traverse to the next page
#using the generated url to get to the next page
#get the necessary address information using lxml


    addressURL = 'http://www.creditunionsonline.com/'+ addressLink[i]
    page = requests.get(addressURL)
    tree = html.fromstring(page.content)

    addressList.append(tree.xpath('//span[@itemprop="streetAddress"]/text()'))
	
    cityList.append(tree.xpath('//span[@itemprop="addressLocality"]/text()'))
    stateList.append(tree.xpath('//span[@itemprop="addressRegion"]/text()'))
    zipcList.append(tree.xpath('//span[@itemprop="postalCode"]/text()'))
    zipCode = tree.xpath('//span[@itemprop="postalCode"]/text()') 
    islandList.append(islandFind(zipCode))
    phoneList.append(tree.xpath('//div[@class="textH"]/span/text()'))

#generate a new new url based on the financeLinks list
#use the generated url to go to the next page
#generate an html tree structure
	
    financeLinks = tree.xpath('//nav[@class="btnWrap"]/a/@href')
#    print(financeLinks[-2])
#    print(type(financeLinks[-2]))

#    if(financeLinks[-2] != '#reviews'):
#        branchLink = financeLinks[-2]
#        page = requests.get(branchLink)
#        tree = html.fromstring(page.content)
#        branchList.append(tree.xpath('//div[@class="secText"]/a[1]/text()')
#        nextPage = requests.get('//div[@class="secText"]/a[0]/href')
#        financeLinks = tree.xpath('//nav[@class="btnWrap"]/a/@href')
#		financeURL = financeLinks[-1]

    financeURL = financeLinks[-1]	
    page = requests.get(financeURL)
    tree = html.fromstring(page.content)

#create a list of all financial information

    finance = tree.xpath('//div[@class="financeTable"]/div[@class="hoursRow"]/div[@class="hoursCell hoursR"]/text()')

#parse the finance list for necessary data

    assetsList.append(finance[2])
    loansList.append(finance[3])
    netWorthList.append(finance[4])
    membersList.append(finance[5])
    fullTimeList.append(finance[6])
    partTimeList.append(finance[7])

#print finance data

   # print(assets)
   # print(loans)
   # print(netWorth)
   # print(members)
   # print(fullTime)
   # print(partTime)		

    print("Data has been collected from {0} Credit Unions\n,".format(i+1))

#go back to the initial page
    
    page = requests.get('https://www.creditunionsonline.com/hawaii-credit-unions.html')
    tree = html.fromstring(page.content)	

print (bNameList)
print (addressList)
print (cityList)
print (stateList)
print (zipcList)
print (islandList)
print (phoneList)
#print (branchList)
print (assetsList)
print (loansList)
print (netWorthList)
print (membersList)
print (fullTimeList)
print (partTimeList)
  
with open("./outputTest.csv", "w", newline='') as fp:
    writer = csv.writer(fp, delimiter = ',')
    for j in range (5):
        writer.writerow([bNameList[j]])
        writer.writerow([addressList[j]]) 
        writer.writerow([cityList[j]])
        writer.writerow([zipcList[j]])
        writer.writerow([islandList[j]])
        writer.writerow([phoneList[j]])
        writer.writerow([assetsList[j]])
        writer.writerow([loansList[j]])
        writer.writerow([netWorthList[j]])
        writer.writerow([membersList[j]])
        writer.writerow([fullTimeList[j]])
        writer.writerow([partTimeList[j]])
