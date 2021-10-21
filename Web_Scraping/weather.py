import requests
from bs4 import BeautifulSoup

city = "Mathura"
url = "https://www.google.com/search?q=" + "weather" + city
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# adjust the formation of the data
data = str.split('\n')
time = data[0]
sky = data[1]
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

# other important feautre of the data
pos = strd.find('Wind')
other_data = strd[pos:]

# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
# comit new data aded
