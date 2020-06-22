#Goal webscrape from newEgg store front to a CSV File

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#download the website
uClient = uReq(url)
pageHtml = uClient.read()
uClient.close()

#print(pageHtml)
pageSoup = soup(pageHtml, "html.parser")
print(pageSoup.h1)

print(pageSoup.body.span)

containers = pageSoup.findAll("div", {'class':'item-container'})
print(len(containers))

container = containers[0]
containerTitle = container.findAll("a", {'class':'item-title'})

filename = '../C_Data/newEggGraphicsCards.csv'
f = open(filename, "w")
headers = "Brand, ProductName, Shipping\n"
f.write(headers)
#print(container)
for container in containers:
    containerBrand = container.findAll("a", {'class':'item-brand'})
    brand = containerBrand[0].img['title']
    print("Product Brand: ", brand )
    containerTitle = container.findAll("a", {'class':'item-title'})
    productName = containerTitle[0].text
    print("Product Name Title: ", productName)
    containerShipping = container.findAll("li", {"class":"price-ship"})
    shippingPrice = containerShipping[0].text.strip()
    print("Shipping Price: ", shippingPrice)
    print("\n")
    f.write(brand + "," + productName.replace(",", "|") + "," + shippingPrice + "\n" )

f.close()
