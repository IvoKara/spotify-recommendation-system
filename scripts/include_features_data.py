from os import path

import numpy as np
import pandas as pd

from auth import spotify
from definitions import FEATURES_PATH, TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.preprocess_data import preprocess
from spotify_types.track import TrackAudioFeatures

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


def fetch_audio_features(track_ids: pd.Series, split_by: int):
    id_chunks: list[pd.Series] = np.array_split(track_ids, split_by)  # type: ignore

    for id_chunk in id_chunks:
        index: pd.RangeIndex = id_chunk.index  # type: ignore
        print(f"Fetching audio features for tracks #{index.start} - #{index.stop}")
        audio_features: list[TrackAudioFeatures] | None = (
            spotify.audio_features(id_chunk.tolist())  # noqa
        )
        if audio_features is None:
            raise Exception("error in audio_features request")

        has_data = path.isfile(FEATURES_PATH)
        mode = "w" if has_data and index.start == 0 else "a"
        header = not has_data or mode == "w"
        audio_df = pd.DataFrame(list(filter(None, audio_features)))
        audio_df.to_csv(FEATURES_PATH, sep=";", mode=mode, header=header, index=False)

    distinct_df = pd.read_csv(FEATURES_PATH, delimiter=";").drop_duplicates()
    distinct_df.to_csv(FEATURES_PATH, sep=";", index=False)


def include_features_to_data():
    df = pd.read_csv(TRACKS_PATH, delimiter=";")
    df = preprocess(df)

    # split into equal parts
    count = len(df.index) // (100 - 2)

    print("fetching audio features for tracks")
    # comment bellow if you already have data
    fetch_audio_features(df["track_id"], count)
    features_df = pd.read_csv(FEATURES_PATH, delimiter=";", usecols=NECESSARY_FEATURES)

    merged_df = pd.merge(df, features_df, left_on="track_id", right_on="id")
    print("with audio features", len(df.index), "tracks")

    print("Saving data locally...")
    merged_df.to_csv(TRACKS_WITH_FEATURES_PATH, sep=";", index=False)
    print("Tracks with features successfully saved")


if __name__ == "__main__":
    include_features_to_data()
