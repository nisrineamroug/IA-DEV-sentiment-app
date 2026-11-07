"""Evaluate the persisted classifier and print its confusion matrix."""
from __future__ import annotations

import pandas as pd
from sklearn.metrics import confusion_matrix

from predict import load_model
from train import DATA_PATH


def main() -> None:
    frame = pd.read_csv(DATA_PATH)
    model = load_model()
    predictions = model.predict(frame["review"])
    matrix = confusion_matrix(frame["label"], predictions, labels=["negative", "positive"])
    print("Matrice de confusion (negative, positive):")
    print(matrix)
    errors = frame.loc[predictions != frame["label"]]
    print(f"Erreurs : {len(errors)}")
    for _, row in errors.head(3).iterrows():
        print(f"- {row['review']} -> attendu {row['label']}, obtenu {predictions[row.name]}")


if __name__ == "__main__":
    main()
