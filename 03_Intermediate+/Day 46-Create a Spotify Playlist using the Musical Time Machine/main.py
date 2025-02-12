import os

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv, find_dotenv
from wsproto.connection import CLIENT

find_path = find_dotenv()
load_dotenv(find_path)
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
CLIENT_URI=os.getenv("URI")


# Scrap From billboard 100
date = input("Which year do you want to travel to? Type the date in this this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

song_title = soup.select("li ul li h3")
song_titles = [title.getText().strip() for title in song_title]
print(song_titles)

# Initialize Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=CLIENT_URI,
    scope ="user-library-read user-library-modify",

))

for title in song_titles:
    result = sp.search(q=f"track: {title}", type="track", limit=1) # Search track by name and get track_id
    if result["tracks"]["items"]:
        track_id = result["tracks"]["items"][0]["id"]
        print(track_id)
        sp.current_user_saved_tracks_add([track_id])
        print(f"Added {track_id} to the playlist")
    else:
        print(f"Track {title} does not exist in the playlist")

print("All tracks processed")