from os import path

from definitions import TRACKS_PATH
from scripts.fetch_data import collect_general_track_data

# from scripts.load_data import prepare

if __name__ == "__main__":
    if not path.isfile(TRACKS_PATH):
        collect_general_track_data()

    print("successfully gained data from Spotify's API")
    # df = pd.read_csv(TRACKS_PATH, delimiter=";")
    # df = prepare(df)

    # print(df.head())
