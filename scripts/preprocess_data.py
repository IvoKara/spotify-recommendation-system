import pandas as pd


def remove_duplicates(df: pd.DataFrame):
    return df.drop_duplicates(subset=["track_id", "genres"])


def merge_by_genre(df: pd.DataFrame):
    return df.groupby("track_id").agg(tuple).map(list).reset_index()


def preprocess(df: pd.DataFrame):
    print("with duplicates ", len(df.index))
    df = remove_duplicates(df)
    print("without duplicates ", len(df.index))

    df = merge_by_genre(df)
    print("after merge", len(df.index))

    return df


# df = pd.read_csv(TRACKS_WITH_FEATURES_PATH, delimiter=";")
# tracks_with_features_df = prepare(df)
