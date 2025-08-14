import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
expected_format = '%Y-%m-%d'
year = expected_format.find('%Y')
is_incorrect_format = True
date = ""

def get_song_uris(name, song_artist):
    song_uris = []
    if len(name) == len(song_artist):
        for index in range(len(name)):
            track = name[index].get_text(strip=True)
            results = sp.search(
                q=f"track:{track} artist:{song_artist[index]}", limit=1)

            if results['tracks']['items']:
                song_uris.append(results['tracks']['items'][0]['uri'])
                print(results['tracks']['items'][0]['uri'])
            else:
                print(f"Song:{track} by {song_artist[index]} could not be found. Skipping...")

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
song_artists = [item.next_sibling.next_sibling for item in song_names]
song_artists_cleaned = []

#Some artists names have different formatting if there are features. This goes through the features and takes the first artist.
for song in song_names:
    artist = song.next_sibling.next_sibling
    if artist.find("a") is not None:
         artist_cleaned = artist.find("a").get_text()
    else:
        artist_cleaned = artist.get_text(strip=True)

    song_artists_cleaned.append(artist_cleaned)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["SPOTIFY_CLIENT_ID"],
    client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
    redirect_uri=os.environ["SPOTIFY_REDIRECT_URI"],
    scope="playlist-modify-private",
))

uris = get_song_uris(song_names, song_artists_cleaned)
user_id= sp.current_user()['id']

new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                        public=False, collaborative=False,
                        description=f"Playlist from the date {date}")

sp.playlist_add_items(playlist_id=new_playlist['id'], items=uris, position=None)

