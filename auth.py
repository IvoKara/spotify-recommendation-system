from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())
