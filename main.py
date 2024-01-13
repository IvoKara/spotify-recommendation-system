from os import path

from definitions import TRACKS_PATH, TRACKS_WITH_FEATURES_PATH
from scripts.fetch_api_data import collect_general_track_data
from scripts.include_features_data import include_features_to_data


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

    # prepare data

    # return prepared data


if __name__ == "__main__":
    load_data()

    # df = pd.read_csv(TRACKS_PATH, delimiter=";")
    # df = prepare(df)
    # print(df.head())
