import numpy as np
import pandas as pd

from auth import spotify
from definitions import TRACKS_PATH
from scripts.preprocess_data import preprocess


def include_features_to_data():
    df = pd.read_csv(TRACKS_PATH, delimiter=";")
    df = preprocess(df)

    id_chunks = np.array_split(df["track_id"][:30], 10)

    audio_features = spotify.audio_features(id_chunks[0])
    print(audio_features)
