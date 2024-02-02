import pandas as pd

from utils import playlist as pl
from utils.log import dlog


class Summarizer:
    def __init__(self, feature_set: pd.DataFrame):
        self._feature_set = feature_set

    def __get_contained(self, playlist_id: str):
        dlog(f"Getting data for playlist({playlist_id}) from Web API...")

        playlist_tracks = pl.get_tracks(playlist_id)
        playlist_track_ids = [track["id"] for track in playlist_tracks]

        contained = self._feature_set["track_id"].isin(playlist_track_ids)
        return contained

    def summarize_playlist(self, playlist_id: str):
        contained = self.__get_contained(playlist_id)
        playlist_with_features = self._feature_set.loc[contained]

        dlog("Summarizing tracks from the playlist into one")
        summarized = playlist_with_features.drop(columns="track_id").sum(axis=0)
        return summarized

    def differentiate_playlist_tracks(self, playlist_id: str):
        contained = self.__get_contained(playlist_id)

        dlog("Removing playlist tracks from the big analisys dataset")
        differetiated_df = self._feature_set.loc[~contained]

        return differetiated_df
