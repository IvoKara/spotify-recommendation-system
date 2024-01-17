import pandas as pd

from definitions import TRACKS_PATH


def remove_duplicates(df: pd.DataFrame):
    return df.drop_duplicates(subset=["track_id", "genres"])


def merge_by_genre(df: pd.DataFrame):
    grouped_df = df.groupby(["track_id"])
    genres_df = grouped_df.agg({"genres": list}).reset_index()
    df = df.drop_duplicates(["track_id"]).drop("genres", axis=1)

    return genres_df.merge(df, on="track_id", how="right")


def preprocess(df: pd.DataFrame):
    print("with duplicates ", len(df.index))
    df = remove_duplicates(df)
    print("without duplicates ", len(df.index))

    df = merge_by_genre(df)
    print("after merge", len(df.index))

    return df


if __name__ == "__main__":
    df = pd.read_csv(TRACKS_PATH, delimiter=";")
    df = preprocess(df)
