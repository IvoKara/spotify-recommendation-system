from recommend.prepare import create_features_set
from scripts import load_data

if __name__ == "__main__":
    df = load_data()

    features_df = create_features_set(df)
    print(features_df.head())
    print(features_df.dtypes)
