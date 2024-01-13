from itertools import chain

import pandas as pd

from constants.genres import subgenres
from definitions import TRACKS_PATH
from utils import playlist as pl
from utils import track as tr


def collect_general_track_data():
    for genre in chain.from_iterable(subgenres):
        print("Searching playlists for - ", genre)
        playlists = pl.search_by_genre(genre)

        print("gettings playlists tracks")
        tracks = pl.get_tracks_from_many(playlists)

        prepared_tracks = list(map(tr.prepare, tracks))
        df = pd.DataFrame.from_dict(prepared_tracks)
        df["genres"] = genre

        # save locally
        print("data saved locally")
        df.to_csv(TRACKS_PATH, sep=";", mode="a", index=False)


# def fetch_with_audio_features():
#     pd.read_csv(TRACKS_PATH, delimiter=";")
