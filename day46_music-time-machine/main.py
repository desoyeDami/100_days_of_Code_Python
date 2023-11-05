import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scrap the top 100 songs according to the specified date
user_request = input("What year do you like to travel to? Type the date is this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_request}")
billboard = response.text
soup = BeautifulSoup(billboard, "html.parser")
top_song = [song.getText().strip() for song in soup.select("li ul li h3")]

# Authenticate your Spotify Account
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="c461b681aff746e6901c83bb0349c47c",
        client_secret="17a52a4124f547f8a8858bab160abdd6",
        show_dialog=True,
        cache_path="token.txt",
        username="Emmanuel Adesoye"
    ))

# Get the uri of the songs scrapped
n = 0
top_song_uri = []
year = user_request.split("-")[0]
while n < len(top_song):
    searched_url = spotify.search(q=f"track: {top_song[n]} year: {year}")
    try:
        top_song_uri.append(searched_url["tracks"]["items"][0]["uri"])
    except FileNotFoundError or IndexError:
        continue
    finally:
        n += 1

# Create a new playlist
user_id = spotify.current_user()["id"]
create_playlist = spotify.user_playlist_create(
    user=f"{user_id}",
    name=f"{user_request} Billboard 100",
    public=False
)
# Add songs to the created play list
spotify.playlist_add_items(playlist_id=create_playlist["id"], items=top_song_uri)
