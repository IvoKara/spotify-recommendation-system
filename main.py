from typing import List, Tuple

import pandas as pd

from auth import spotify
from utils.url import url_to_id

if __name__ == "__main__":
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

    df = pd.DataFrame(data=set(tracks_info), columns=["track_id", "genres"])
    df.to_csv("./data/tracks_info.csv", index=False)

    df = df.groupby("track_id")["genres"].apply(list).reset_index()
    print(df.head())
# tracks_number = sum([playlist['tracks']['total'] for playlist in playlists])
# print(tracks_number)
