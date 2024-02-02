import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from utils.log import dlog, ilog, slog


def calculate_similarity(vectorized_playlist: pd.Series, df: pd.DataFrame):
    numpy_representation = df.drop("track_id", axis=1).to_numpy()
    # making it array of arrays (1, 53) instead of (53, )
    dlog("Reshaping the vectorized playlist")
    reshaped_playlist = vectorized_playlist.to_numpy().reshape(1, -1)

    ilog("Calculating cosine similarity...")
    similarity = cosine_similarity(numpy_representation, reshaped_playlist)
    slog("Similarities generated")

    # undo the array of arrays thing
    df["similarity"] = similarity[:, 0]

    dlog("Ordering dataset by similarity by descending")
    ordered_recommendations = df.sort_values("similarity", ascending=False)
    return ordered_recommendations
