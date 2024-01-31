from recommend.prepare import create_features_set
from recommend.process.summarize import Summarizer
from scripts import load_data

if __name__ == "__main__":
    df = load_data()

    features_df = create_features_set(df)
    print(features_df.head())
    print(features_df.dtypes)
    s = Summarizer(features_df)
    playlist_id = "51KBdMmUmcEHfmuKp6GahJ"
    print(s.summarize_playlist(playlist_id))
    print(s.differentiate_playlist_tracks(playlist_id))
