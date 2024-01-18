from typing import Optional

import pandas as pd


def one_hot_encoding(
    df: pd.DataFrame,
    column: str,
    new_name: Optional[str] = None,
):
    if new_name is None:
        new_name = column

    # True/False table
    dummies_df = pd.get_dummies(df[column])
    column_names = dummies_df.columns
    dummies_df.columns = [f"{new_name}|{col}" for col in column_names]
    return dummies_df.reset_index(drop=True)
