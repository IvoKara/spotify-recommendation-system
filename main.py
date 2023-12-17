from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from constants.playlist import top_songs_id

spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())

result = spotify.playlist(top_songs_id)

print(f"\"{result['name']}\" playlist by {result['owner']['display_name']}")