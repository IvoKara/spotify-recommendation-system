from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from typing import Set

from constants.playlist import top_songs_id
from utils.url import url_to_id

spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())

result = spotify.playlist(top_songs_id)


if __name__ == "__main__":
    track_ids: Set[str] = set([])
    for i in 0, 50:
        search = spotify.search("slap house", offset=i, limit=50, type="playlist")
        playlists = search["playlists"]["items"]
        for playlist in playlists:
            print(f'{playlist["name"]} - {playlist["tracks"]["total"]} tracks total')
            playlist_id = url_to_id(playlist["href"])
            print(playlist_id)

            playlist_data = spotify.playlist_tracks(
                playlist_id, fields="items(track(id,name))"
            )

            items = filter(lambda x: x["track"] is not None, playlist_data["items"])
            track_ids.update({item["track"]["id"] for item in items})

    print(len(track_ids))
    # tracks_number = sum([playlist['tracks']['total'] for playlist in playlists])
    # print(tracks_number)
