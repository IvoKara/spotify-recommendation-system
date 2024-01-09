from typing import List, Tuple

from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

from utils.url import url_to_id

spotify = Spotify(client_credentials_manager=SpotifyClientCredentials())


if __name__ == "__main__":
    # df = pd.DataFrame(columns=["track_id", "track_name", "artists", "genres"])
    tracks_info: List[Tuple[str, str]] = []
    genre = "slap house"
    for i in 0, 50, 100:
        print(i)
        search = spotify.search(genre, offset=i, limit=50, type="playlist")
        playlists = search["playlists"]["items"]

        for playlist in playlists:
            # print(f'{playlist["name"]} - {playlist["tracks"]["total"]} tracks total')

            playlist_id = url_to_id(playlist["href"])
            # print(playlist_id)

            playlist_tracks = spotify.playlist_tracks(
                playlist_id, fields="items(track(id))"
            )["items"]

            tracks_info.extend(
                [
                    (item["track"]["id"], genre)
                    for item in playlist_tracks
                    if item["track"] is not None
                ]
            )

    print(len(set(tracks_info)))
    # tracks_number = sum([playlist['tracks']['total'] for playlist in playlists])
    # print(tracks_number)
