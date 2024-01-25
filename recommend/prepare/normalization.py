import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def normalize(df: pd.DataFrame, columns: list[str]):
    # needs to by matrix-like for scaler.fit_transform
    series = df[columns].reset_index(drop=True)

    scaler = MinMaxScaler()
    normalized = pd.DataFrame(scaler.fit_transform(series), columns=series.columns)

    return normalized
