#!/usr/bin/python3


#Authors: Isaac DeMello, Jie Zhou, Wendy Chong
#cuinfo.py - Saves specific info about credit unions across Hawaii

from lxml import html
import requests
import csv


#islandFind takes in a zip code
#returns the corresponding island the credit union is on
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

#list initialization before the loop
addressList = []
cityList= []
stateList= []
zipcList = []
islandList = []
phoneList = []
branchList = []
assetsList = []
nwRatioList =[]
wcList = []
loansList = []
netWorthList = []
membersList = []
fullTimeList = []
partTimeList = []
assetList = [] #initalize new lists for output
loanList = []

for i in range(61):

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
    phoneList.append(tree.xpath('//div[@class="textH"][1]/span/text()'))

#generate a new new url based on the financeLinks list
#use the generated url to go to the next page
#generate an html tree structure
	
    financeLinks = tree.xpath('//nav[@class="btnWrap"]/a/@href')
    print(financeLinks[-2])
    print(type(financeLinks[-2]))

    if(financeLinks[-2] != '#reviews'):
        branchList.append('Yes')
    else:
        branchList.append('No')
#        page = requests.get(branchLink)
#        tree = html.fromstring(page.content)
#        branchList.append(tree.xpath('//div[@class="secText"]/a[1]/text()')

    financeURL = financeLinks[-1]	
    page = requests.get(financeURL)
    tree = html.fromstring(page.content)

#create a list of all financial information

    finance = tree.xpath('//div[@class="financeTable"]/div[@class="hoursRow"]/div[@class="hoursCell hoursR"]/text()')

#parse the finance list for necessary data

    assetsList.append(finance[1])
    loansList.append(finance[2])
    netWorthList.append(finance[3])
    wcList.append(finance[4])
    membersList.append(finance[5])
    fullTimeList.append(finance[6])
    partTimeList.append(finance[7])

# change assests and loans string format to purely numbers for calculation
# and change back to string for output
    if " " in assetsList[i]:
        assets = assetsList[i].split(" ")

        assets1 = assets[0].replace("$","")
        assets2 = assets[1]
        if assets2 == "Billion":
            assets2 = 1000000000
        elif assets2 == "Million":
            assets2= 1000000

        asset = float(assets1) * assets2 #convert to float for calculation
        assetOut = str(asset) #convert from float back to string
    else:
        asset = str(assetsList)
        assetOut = asset.replace("$","")

    if " " in loansList[i]:
        loans = loansList[i].split(" ")

        loans1 = loans[0].replace("$","")
        loans2 = loans[1]
        if loans2 == "Billion":
            loans2 = 1000000000
        elif loans2 == "Million":
            loans2 = 1000000

        loan = float(loans1) * loans2 #same convertion as assetsList
        loanOut = str(loan) #same convertion as assetsList
    else:
        loan = str(loansList)
        loanOut = loan.replace("$","")


    assetList.append(assetOut)
    loanList.append(loanOut)


#print finance data
#remove #'s for debugging

#    print(assetList) #[i] component addressed in the above code
#    print(loanList) #[i] component addressed in the above code
#    print(netWorthList[i])
#    print(wcList[i])
#    print(membersList[i])
#    print(fullTimeList[i])
#    print(partTimeList[i])

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
print (branchList)
print (assetList)
print (loanList)
print (netWorthList)
print (wcList)
print (membersList)
print (fullTimeList)
print (partTimeList)
  
#open a .csv file using the imported csv module
#create the headings for all colums
#define the writer to add values that exist between commas

with open("./CreditUnionData.csv", "w", newline='') as fp:
    writer = csv.writer(fp, delimiter = ',')
    writer.writerow((['Name', 'Address', 'City', 'Zip Code', 'Island', 'Phone Number', 'Multiple Branches', 'Assets', 'Well Capitalized', 'Loans', 'Net Worth', 'Number of Members', 'Full Time Employees', 'Part Time Employees']))
#create a ziplist to hold all scraped data

    rows = zip(bNameList, addressList, cityList, zipcList, islandList, phoneList, branchList, assetList, wcList, loanList, netWorthList, membersList, fullTimeList, partTimeList )

#iterate through all the rows until data is correctly displayed within excel
    for row in rows:
        writer.writerow(row)

