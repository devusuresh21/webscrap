import pandas as pd
import requests
from bs4 import BeautifulSoup

product_names = []
prices = []

url = "https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.brand%255B%255D%3DMi&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_TVs%20%26%20Appliances_0_Mi"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("div", class_="_4rR01T")
for name in names:
    product_names.append(name.text)

prices_elements = soup.find_all("div", class_="_30jeq3")
for price_element in prices_elements:
    prices.append(price_element.text)

if len(product_names) != len(prices):
    raise ValueError("The lengths of product_names and prices do not match")

df = pd.DataFrame({"Product Name": product_names, "Prices": prices})

# Print the DataFrame to verify the data
print(df)

# Save the DataFrame to a CSV file
csv_file_path = "C:\\Users\\Arjun\\Desktop\\day2 programs\\flipkart.csv"
df.to_csv(csv_file_path, index=False)  # Set index=False to exclude index column

print(f"CSV file saved at: {csv_file_path}")
