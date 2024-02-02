from recommend.process import generate_recommendations
from scripts import load_data


def recommend_from_playlist(playlist_id: str, count: int = 10):
    df = load_data()
    recommendations = generate_recommendations(df, playlist_id)

    return recommendations.head(count)
