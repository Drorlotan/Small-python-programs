import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/Amazon-Essentials-Standard-Heavy-Weight-Puffer/dp/B07PY4WQ6S/ref=sr_1_1_sspa?crid" \
      "=N1CWFFAJKCV1&keywords=vest+coat+for+men&qid=1643218618&sprefix=vest+coat%2Caps%2C210&sr=8-1-spons&psc=1&spLa" \
      "=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUENRWDhDWkNVQTVIJmVuY3J5cHRlZElkPUEwNTUyMjYwMkZLR0hKU0hJVzdPSiZlbmNyeXB0ZWRBZElk" \
      "PUEwNjQ3NjM4M1ZLSkZIQlE0NE5DNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU= "
headers = {
    "Accept-Language": "he,en-US;q=0.9,en;q=0.8",
    "Content-Type": "text",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
}

response = requests.get(URL, headers=headers)
website = response.text
soup = BeautifulSoup(website, "lxml")
price_tag = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
if price_tag < 25:
    print("go by yourself a vest, its really low price now!")
