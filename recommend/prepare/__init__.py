from os import path

import pandas as pd

from definitions import ROOT_DIR
from utils.log import dlog, ilog, slog

from .normalization import normalize
from .one_hot_encoding import one_hot_encoding
from .sentiment import sentiment_analysis
from .tf_idf import tf_idf

FEATURES_SET_PATH = path.join(ROOT_DIR, "data/features_set.csv")


def create_features_set(df: pd.DataFrame):
    if path.isfile(FEATURES_SET_PATH):
        ilog("Using locally saved feature set")
        return pd.read_csv(FEATURES_SET_PATH, delimiter=";")

    ilog("TF-IDF analisys according to genres data")
    genre_df = tf_idf(df, "genres")
    slog("Successfully got trough TF_IDF")

    ilog("Sentiment analysis for every track name")
    sentiment_df = sentiment_analysis(df, "track_name")
    slog("Successfully got made sentiment")

    ilog("One-hot encoding for various features: subjectivity, polarity, key, mode")
    subjectivity_df = one_hot_encoding(sentiment_df, "subjectivity")
    polarity_df = one_hot_encoding(sentiment_df, "polarity")
    key_df = one_hot_encoding(df, "key")
    mode_df = one_hot_encoding(df, "mode")
    slog("One-hot encoding done well")

    ilog("Normalize all float values")
    float_columns: list[str] = df.dtypes[df.dtypes == "float64"].index.values  # type: ignore
    normalized_df = normalize(df, float_columns)
    slog("Successful normalization")

    ilog("Summing up all the data in one place")
    featured_df = pd.concat(
        [
            genre_df,
            subjectivity_df,
            polarity_df,
            key_df,
            mode_df,
            normalized_df,
        ],
        axis=1,
    )

    featured_df["track_id"] = df["track_id"]

    dlog(f"Tracks after concatination: {len(featured_df.index)}")

    dlog("Saving feature set locally...")
    featured_df.to_csv(FEATURES_SET_PATH, sep=";", index=False)

    return featured_df
