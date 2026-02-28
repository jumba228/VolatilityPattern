from sklearn.cluster import KMeans
import numpy as np

from src.data.loader import DataLoader


def build_dummy_features(df):
    df["range"] = df["high"] - df["low"]
    return df[["range"]].dropna()


def main():
    loader = DataLoader("data/sample/sample_btc_1h.csv")
    df = loader.load()

    features = build_dummy_features(df)

    model = KMeans(n_clusters=3, random_state=42)
    labels = model.fit_predict(features)

    print("Cluster counts:")
    print(np.bincount(labels))


if __name__ == "__main__":
    main()