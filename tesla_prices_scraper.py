from bs4 import BeautifulSoup
import requests
url = requests.get("https://www.marketwatch.com/investing/stock/tsla")
bsp = BeautifulSoup(url.text, "html.parser")
print(bsp.title.text)

cprice = bsp.find_all(class_ = 'intraday__price')
tstamp = bsp.find_all(class_ = 'intraday__timestamp')
crate = bsp.find_all(class_ = 'change--percent--q')

for price in cprice:
    price = cprice[0].text

for time in tstamp:
    time = tstamp[0].text

for change in crate:
    change = crate[0].text
print("Current tesla stock prices is " + price.strip())
print("ROC of tesla stock prices is " + change.strip())
print(time.strip())
