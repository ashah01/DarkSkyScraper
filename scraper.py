import requests
from bs4 import BeautifulSoup

url = "https://darksky.net/forecast/43.7117,-79.3683/si12/en"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                         "Version/13.1 Safari/605.1.15"}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
weather = soup.find('span', {"class": "summary swap"}).get_text()
feels_like = soup.find('span', {"class": "feels-like-text"}).get_text()
low = soup.find('span', {"class": "low-temp-text"}).get_text()
high = soup.find('span', {"class": "high-temp-text"}).get_text()

print(f"{weather} | Feels Like: {feels_like} | Low: {low} | High: {high}")
