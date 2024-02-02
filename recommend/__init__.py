from recommend.process import generate_recommendations
from scripts import load_data
from utils.log import ilog, slog


def recommend_from_playlist(playlist_id: str, count: int = 10):
    df = load_data()

    ilog("Trying to get the best recommendations...")
    recommendations = generate_recommendations(df, playlist_id)
    slog("Recommendations are ready!")

    return recommendations.head(count)
