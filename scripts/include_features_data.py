import numpy as np
import pandas as pd

from auth import spotify
from definitions import TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.preprocess_data import preprocess
from spotify_types import TrackAudioFeatures

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
    id_chunks = np.array_split(track_ids, split_by)

    audio_features: list[TrackAudioFeatures] = []
    for id_chunk in id_chunks:
        temp_features: list[TrackAudioFeatures] | None = (
            spotify.audio_features(id_chunk.tolist())  # noqa
        )
        if temp_features is None:
            raise Exception("error in audio_features request")

        audio_features.extend(temp_features)

    return audio_features


def include_features_to_data():
    df = pd.read_csv(TRACKS_PATH, delimiter=";")
    df = preprocess(df)

    # split into equal parts
    count = len(df.index) // 80 + 1

    print("fetching audio features for tracks")
    audio_features = fetch_audio_features(df["track_id"], count)
    features_df = pd.DataFrame(audio_features, columns=NECESSARY_FEATURES)

    df = df.merge(features_df, left_on="track_id", right_on="id")
    print("with audio features", len(df.index), "tracks")

    print("Saving data locally...")
    df.to_csv(TRACKS_WITH_FEATURES_PATH, sep=";", index=False)
    print("Tracks with features successfully saved")


if __name__ == "__main__":
    include_features_to_data()
