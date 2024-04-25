import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
movie_titles = [title.getText() for title in movies]
movies_order = movie_titles[::-1]

with open('movies_order.txt', 'w') as file:
    for title in movies_order:
        file.write(f"{title}\n")
