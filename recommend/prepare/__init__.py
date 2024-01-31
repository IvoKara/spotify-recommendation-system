import pandas as pd

from .normalization import normalize
from .one_hot_encoding import one_hot_encoding
from .sentiment import sentiment_analysis
from .tf_idf import tf_idf


def create_features_set(df: pd.DataFrame):
    # TF-IDF for genres list
    genre_df = tf_idf(df, "genres")

    # Sentiment analysis for tracks name
    sentiment_df = sentiment_analysis(df, "track_name")

    # One-hot encoding for various features
    subjectivity_df = one_hot_encoding(sentiment_df, "subjectivity")
    polarity_df = one_hot_encoding(sentiment_df, "polarity")
    key_df = one_hot_encoding(df, "key")
    mode_df = one_hot_encoding(df, "mode")

    # Normalize all float values
    float_columns: list[str] = df.dtypes[df.dtypes == "float64"].index.values  # type: ignore
    normalized_df = normalize(df, float_columns)

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

    return featured_df
