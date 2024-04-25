import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

song_title = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in song_title]
print(song_titles)






