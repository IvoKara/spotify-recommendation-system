import pandas as pd
from textblob import TextBlob


def subjectivity(text: str) -> float:
    return TextBlob(text).subjectivity  # type: ignore


def polarity(text: str) -> float:
    return TextBlob(text).polarity  # type: ignore


def categorize_subjectivity(score: float):
    if score < 1 / 3:
        return "low"
    elif score > 1 / 3:
        return "high"
    else:
        return "medium"


def categorize_polarity(score: float):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"


def sentiment_analysis(df: pd.DataFrame, column: str):
    sentiment_df = pd.DataFrame(
        {
            "subjectivity": (
                df[column]
                .apply(subjectivity)  # noqa
                .apply(categorize_subjectivity)
            ),
            "polarity": (
                df[column]
                .apply(polarity)  # noqa
                .apply(categorize_polarity)
            ),
        }
    )

    return sentiment_df
