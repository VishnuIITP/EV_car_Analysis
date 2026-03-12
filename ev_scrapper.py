import requests
from bs4 import BeautifulSoup

url = "https://www.cardekho.com/electric-cars"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

cars = soup.find_all("div", class_ = "gsc_col-xs-12 holder truncate")

names = []
prices = []
ranges = []
powers = []
batteries = []

for car in cars:
    name= car.find("a").text
    price = car.find("div", class_='price').text.strip()
    specs = car.find("div", class_="dotlist BottomMarginRemove")

    if specs:
        values = [v.text.strip() for v in specs.find_all('span')]

    else:
        values = []

    names.append(name)
    prices.append(price)

    if len(values) >= 3:
        ranges.append(values[0])
        powers.append(values[1])
        batteries.append(values[2])

    else:
        ranges.append(None)
        powers.append(None)
        batteries.append(None)


    #print(name,"|",price,"|",values)

import pandas as pd

df = pd.DataFrame(
    {"Car_Name": names,
     "Price": prices,
     "Range": ranges,
     "Power": powers,
     "Battery": batteries}
)

print(df.head())

df.to_csv("ev_cars.csv",index = False)