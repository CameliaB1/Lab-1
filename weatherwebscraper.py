from bs4 import BeautifulSoup
import requests

city = input("Please enter the city you would like to search: ")
state = input("Which state is that city located?: ")

url = requests.get("https://weather.com/weather/tenday/l/{city}+{state}?canonicalCityId=2793e44da479328c35f16aaab4bd1a229f11b2dac0caef70d1e9334fbfd08c3b")
bsp = BeautifulSoup(url.text, "html.parser")

ddata = bsp.find_all("span", class_ = 'DailyContent--daypartDate--2A3Wi')
tdata = bsp.find_all("span", class_ = 'DailyContent--temp--3d4dn')
pdata = bsp.find_all("span", class_ = 'DailyContent--value--37sk2')
wdata = bsp.find_all("span", class_ = 'Wind--windWrapper--3aqXJ DailyContent--value--37sk2')    

for days in ddata:
    days = ddata[0].text
  
for temps in tdata:
    mtemp = tdata[0].text
    ntemp = tdata[1].text

for percips in pdata:
    mpercips = pdata[0].text
    npercips = pdata[2].text

for wind in wdata:
    wind = wdata[0].text

print("On " + days + " the temperature in the morning is " + mtemp + " and the temperature at night will be " + ntemp + ".")
print("The chance of percipitation in the morning is " + mpercips + " and at night there will be a " + npercips + " chance of percipitation.")
print("Wind will be coming " + wind + ".")
