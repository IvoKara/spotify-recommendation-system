from os import path

from definitions import TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.fetch_api_data import collect_general_track_data
from scripts.include_features_data import include_features_to_data
from scripts.use_local_data import use_local_data


def load_data():
    if not path.isfile(TRACKS_WITH_FEATURES_PATH):
        if not path.isfile(TRACKS_PATH):
            print("No basic track date. Calling the API...")
            collect_general_track_data()
            print("Successfully gained data from Spotify's API")
        else:
            print("There is some local data here. Using it...")

        print("Now adding audio features to the tracks...")
        include_features_to_data()

    print("Using locally saved data")
    return use_local_data()
