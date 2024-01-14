import pandas as pd

from definitions import TRACKS_WITH_FEATURES_PATH


def reformat(df: pd.DataFrame, column: str):
    """
    Convert list columns from stringified list to actial list
    """
    artists_column = df[column]
    df[column] = artists_column.apply(lambda a: a.strip("[]").split(","))

    return df


def use_local_data():
    df = pd.read_csv(TRACKS_WITH_FEATURES_PATH, delimiter=";")
    df = reformat(df, "artists")
    df = reformat(df, "genres")

    return df
