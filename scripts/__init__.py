from os import path

from definitions import FEATURES_PATH, TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.fetch_api_data import collect_general_track_data
from scripts.include_features_data import Fetcher
from scripts.use_local_data import use_local_data
from utils.log import ilog, slog, wlog


def load_data():
    if path.isfile(TRACKS_WITH_FEATURES_PATH):
        ilog("Using locally saved data.")
        return use_local_data()

    has_tracks = path.isfile(TRACKS_PATH)
    has_features = path.isfile(FEATURES_PATH)
    fetcher = Fetcher()

    if not has_tracks:
        wlog("There is no track data.")
        ilog("Calling Spotify's Web API.")

        collect_general_track_data()

        slog("Successfully dowloaded track data from Spotify!")

    if not has_features:
        wlog("There is no audio features data.")
        ilog("Now calling the Web API to get tracks' audio features.")

        fetcher.fetch_audio_features()

        slog("Successfully dowloaded track data from Spotify!")
    elif has_features and not has_tracks:
        wlog(
            "There is audio features data but it does not correspond to current tracks."
        )
        ilog("Now calling the Web API to get tracks' audio features.")

        fetcher.fetch_audio_features()

        slog("Successfully dowloaded track data from Spotify!")
    else:
        wlog(
            "There is no complete data for analysis, but don't worry, contructing it on the way."
        )

    ilog("Including audio features in tracks data...")

    fetcher.include_features_to_tracks()

    slog("Successfully added features to tracks!")

    return use_local_data()
