import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(vectorized_playlist: pd.Series, df: pd.DataFrame):
    numpy_representation = df.drop("track_id", axis=1).to_numpy()
    # making it array of arrays (1, 53) instead of (53, )
    reshaped_playlist = vectorized_playlist.to_numpy().reshape(1, -1)

    similarity = cosine_similarity(numpy_representation, reshaped_playlist)

    # undo the array of arrays thing
    df["similarity"] = similarity[:, 0]

    ordered_recommendations = df.sort_values("similarity", ascending=False)
    return ordered_recommendations
