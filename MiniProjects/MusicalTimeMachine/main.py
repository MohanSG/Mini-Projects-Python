import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

expected_format = '%Y-%m-%d'
is_incorrect_format = True
date = ""

while is_incorrect_format:
    date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
    try:
        datetime.strptime(date, expected_format)
    except ValueError:
        print("The date entered is not valid")
        os.system('cls')
    else:
        is_incorrect_format = False

URL = f"https://www.billboard.com/charts/hot-100/{date}/"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0"
}
response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

chart_results = soup.find_all(name="li", class_="o-chart-results-list__item")
for results in chart_results:
    if results is not None:
        song_title = results.find("h3")
        if song_title is not None:
            print(song_title.get_text(strip=True))



