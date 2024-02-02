from os import path

import numpy as np
import pandas as pd

from auth import spotify
from definitions import FEATURES_PATH, TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.preprocess_data import preprocess
from spotify_types.track import TrackAudioFeatures
from utils.log import dlog

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


class Fetcher:
    def __init__(self):
        tracks_df = pd.read_csv(TRACKS_PATH, delimiter=";")
        self._tracks_df = preprocess(tracks_df)

    @property
    def track_df(self):
        return self._tracks_df

    @property
    def split_by(self):
        return len(self._tracks_df.index) // (100 - 2)

    def fetch_audio_features(self):
        track_ids = self._tracks_df["track_id"]
        id_chunks: list[pd.Series] = np.array_split(track_ids, self.split_by)  # type: ignore

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
            audio_df.to_csv(
                FEATURES_PATH, sep=";", mode=mode, header=header, index=False
            )

        distinct_df = pd.read_csv(FEATURES_PATH, delimiter=";").drop_duplicates()
        distinct_df.to_csv(FEATURES_PATH, sep=";", index=False)

    def include_features_to_tracks(self):
        features_df = pd.read_csv(
            FEATURES_PATH, delimiter=";", usecols=NECESSARY_FEATURES
        )

        merged_df = pd.merge(
            self._tracks_df, features_df, left_on="track_id", right_on="id"
        )

        dlog(f"Tracks with audio features {len(self._tracks_df.index)}")
        merged_df.to_csv(TRACKS_WITH_FEATURES_PATH, sep=";", index=False)


if __name__ == "__main__":
    fetcher = Fetcher()
    fetcher.fetch_audio_features()
    fetcher.include_features_to_tracks()
