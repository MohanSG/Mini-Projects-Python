import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

load_dotenv()
expected_format = '%Y-%m-%d'
year = expected_format.find('%Y')
is_incorrect_format = True
date = ""

def get_song_uris(name, artist):
    song_uris = []
    if len(name) == len(artist):
        for index in range(len(name)):
            track = name[index].get_text(strip=True)
            results = sp.search(
                q=f"track:{track} artist:{artist[index]}", limit=1)

            if results['tracks']['items']:
                song_uris.append(results['tracks']['items'][0]['uri'])
                print(results['tracks']['items'][0]['uri'])
            else:
                print(f"Song:{track} by {artist[index]} could not be found. Skipping...")


    return song_uris

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

song_names = soup.select("li ul li h3")
song_artists = [item.next_sibling.next_sibling.get_text(strip=True) for item in song_names]

print(f"{len(song_names)}")
print(f"{len(song_artists)}")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["SPOTIFY_CLIENT_ID"],
    client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
    scope="user-library-read",
))

uris = get_song_uris(song_names, song_artists)
# results = sp.search(q=f"track:{song_names[4].get_text(strip=False)} artist:{song_artists[4]}")
# print(results)