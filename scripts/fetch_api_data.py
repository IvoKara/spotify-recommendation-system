from itertools import chain
from os import path

import pandas as pd

from constants.genres import subgenres
from definitions import TRACKS_PATH
from utils import playlist as pl
from utils import track as tr


def collect_general_track_data():
    flattened_genres = chain.from_iterable(subgenres)
    for i, genre in enumerate(flattened_genres):
        print("Searching playlists for - ", genre)
        playlists = pl.search_by_genre(genre)

        print("gettings playlists tracks")
        tracks = pl.get_tracks_from_many(playlists)

        prepared_tracks = list(map(tr.prepare, tracks))
        df = pd.DataFrame(prepared_tracks)
        df["genres"] = genre

        # save locally
        has_data = path.isfile(TRACKS_PATH)
        mode = "w" if has_data and i == 0 else "a"
        header = not has_data or mode == "w"
        df.to_csv(TRACKS_PATH, sep=";", mode=mode, header=header, index=False)
    print("data saved locally")


if __name__ == "__main__":
    collect_general_track_data()
