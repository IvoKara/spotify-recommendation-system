from os import path

import pandas as pd

from definitions import LOCAL_DATA_DIR
from utils import playlist as pl


def prepare(track: dict) -> dict:
    prepared = {
        "track_id": track["id"],
        "track_name": track["name"],
        "artists": [artist["name"] for artist in track["artists"]],
        "image_url": track["album"]["images"][0]["url"],
        "release_date": track["album"]["release_date"],
    }

    return prepared


if __name__ == "__main__":
    genre = "slap house"

    print("Searching playlists")
    playlists = pl.search_by_genre(genre)

    print("gettings playlists tracks")
    tracks = pl.get_tracks_from_many(playlists)

    prepared_tracks = list(map(lambda x: prepare(x["track"]), tracks))

    df = pd.DataFrame.from_dict(prepared_tracks)
    print("with duplicates: ", len(df.index))
    df["genres"] = genre

    df = df.drop_duplicates(subset=["track_id", "genres"])
    print("without duplicates: ", len(df.index))

    filepath = path.join(LOCAL_DATA_DIR, "tracks.csv")
    df.to_csv(filepath, sep=";", mode="a", index=False)

    df = df.groupby("track_id")["genres"].apply(list).reset_index()
    print(df.head())
# tracks_number = sum([playlist['tracks']['total'] for playlist in playlists])
# print(tracks_number)
