import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/simple/'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

country_names = soup.find_all("h3", class_="country-name")

names = [name.contents[2].strip() for name in country_names]
print(names)