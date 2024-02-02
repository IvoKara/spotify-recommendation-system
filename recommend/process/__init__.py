import pandas as pd

from ..prepare import create_features_set
from .similarity import calculate_similarity
from .summarize import Summarizer


def generate_recommendations(tracks_df: pd.DataFrame, playlist_id: str):
    features_df = create_features_set(tracks_df)

    s = Summarizer(features_df)
    vectorized = s.summarize_playlist(playlist_id)
    diff = s.differentiate_playlist_tracks(playlist_id)

    return calculate_similarity(vectorized, diff)
