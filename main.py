import pandas as pd

from definitions import TRACKS_PATH
from utils import playlist as pl
from utils import track as tr

if __name__ == "__main__":
    genre = "slap house"

    print("Searching playlists")
    playlists = pl.search_by_genre(genre)

    print("gettings playlists tracks")
    tracks = pl.get_tracks_from_many(playlists)
    prepared_tracks = [tr.prepare(x["track"]) for x in tracks]

    df = pd.DataFrame.from_dict(prepared_tracks)
    print("with duplicates: ", len(df.index))
    df["genres"] = genre

    df = df.drop_duplicates(subset=["track_id", "genres"])
    print("without duplicates: ", len(df.index))

    df.to_csv(TRACKS_PATH, sep=";", mode="a", index=False)

    df = df.groupby("track_id")["genres"].apply(list).reset_index()
    print(df.head())
# tracks_number = sum([playlist['tracks']['total'] for playlist in playlists])
# print(tracks_number)
