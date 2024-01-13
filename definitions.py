from os import path

ROOT_DIR = path.dirname(path.abspath(__file__))  # This is Project Root
LOCAL_DATA_DIR = path.join(ROOT_DIR, "data")

TRACKS_PATH = path.join(LOCAL_DATA_DIR, "tracks_basis.csv")
TRACKS_WITH_FEATURES_PATH = path.join(LOCAL_DATA_DIR, "tracks_with_features.csv")
