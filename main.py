from recommend.prepare import create_features_set
from recommend.process import generate_recommendations
from recommend.process.summarize import Summarizer
from scripts import load_data

if __name__ == "__main__":
    df = load_data()

    features_df = create_features_set(df)
    print(features_df.head())
    print(features_df.dtypes)
    s = Summarizer(features_df)
    playlist_id = "51KBdMmUmcEHfmuKp6GahJ"
    vectorized = s.summarize_playlist(playlist_id)
    diff = s.differentiate_playlist_tracks(playlist_id)
    top_10 = generate_recommendations(vectorized, diff)
    a = df.loc[df["track_id"].isin(top_10["track_id"])]
    print(a[["track_id", "genres", "track_name", "artists"]])
