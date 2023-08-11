import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name=[]
Prices=[]
Description=[]
Reviews=[]
url="https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.brand%255B%255D%3DMi&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Mi"
r=requests.get(url)
#print(r)
soup=BeautifulSoup(r.text,"lxml")
names=soup.find_all("div",class_="_4rR01T")
for i in names:
    name=i.text
    product_name.append(name)
print(product_name)
Prices=soup.find_all("div",class_="30jeq3 _1_WHN1")    
for i in Prices:
    name=i.text
    Prices.append(name)
print(Prices)    

