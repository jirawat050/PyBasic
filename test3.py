import requests
from bs4 import BeautifulSoup

url = "https://www.traveloka.com/th-th/hotel/thailand/region/bangkok-10000045"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#tb = soup.find('div', class_='popularHotelListBox')
#sr_item
for link in soup.select('.popularHotelListBox h3 a'):

    print(link['href'], " + ",link.get_text(strip=True))