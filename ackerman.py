from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get("https://catalog.data.gov/dataset")
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find_all("ul", attrs={"class": "dataset-list unstyled"})

for u in title:
    this = soup.find_all("li", attrs={"class": "dataset-item has-organization"})
    print(len(this))
