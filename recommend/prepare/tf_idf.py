import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(df: pd.DataFrame, column: str):
    joined = df[column].apply(lambda x: " ".join(x))

    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\S\S+")
    tf_idf_matrix = vectorizer.fit_transform(joined)

    custom_df = pd.DataFrame(tf_idf_matrix.toarray())  # type: ignore
    custom_df.columns = [
        f"{column}|{name}" for name in vectorizer.get_feature_names_out()
    ]
    custom_df.reset_index(drop=True, inplace=True)

    return custom_df
