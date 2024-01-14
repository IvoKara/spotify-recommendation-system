import numpy as np
import pandas as pd

from auth import spotify
from definitions import TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.preprocess_data import preprocess

NECESSARY_FEATURES = [
    "id",
    "acousticness",
    "danceability",
    "duration_ms",
    "energy",
    "instrumentalness",
    "key",
    "liveness",
    "loudness",
    "mode",
    "speechiness",
    "tempo",
    "time_signature",
    "valence",
]


def fetch_audio_features(track_ids: list):
    pass


def include_features_to_data():
    df = pd.read_csv(TRACKS_PATH, delimiter=";")
    df = preprocess(df)

    # TODO: use `np.split()` instead
    id_chunks = np.array_split(df["track_id"], 100)

    print("fetching audio features for tracks")
    audio_features = []
    for track_ids in id_chunks:
        audio_features.extend(spotify.audio_features(track_ids))

    features_df = pd.DataFrame(audio_features, columns=NECESSARY_FEATURES)

    df = df.merge(features_df, left_on="track_id", right_on="id", how="left")
    print("with audio features", len(df.index), "tracks")

    print("Saving data locally...")
    df.to_csv(TRACKS_WITH_FEATURES_PATH, sep=";", index=False)
    print("Tracks with features successfully saved")
