import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize(df: pd.DataFrame, column: str):
    # needs to by matrix-like for scaler.fit_transform
    series = df[[column]].reset_index(drop=True)

    scaler = MinMaxScaler()
    normalized = pd.DataFrame(scaler.fit_transform(series), columns=series.columns)

    return normalized
