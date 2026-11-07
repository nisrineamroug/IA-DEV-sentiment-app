"""Display the abstention threshold trade-off."""
from __future__ import annotations

import pandas as pd
from sklearn.metrics import f1_score

from predict import load_model
from train import DATA_PATH


def main() -> None:
    frame = pd.read_csv(DATA_PATH)
    model = load_model()
    probabilities = model.predict_proba(frame["review"])
    confidence = probabilities.max(axis=1)
    predictions = model.classes_[probabilities.argmax(axis=1)]
    for threshold in (0.50, 0.60, 0.70, 0.80):
        accepted = confidence >= threshold
        errors = int(((predictions != frame["label"]) & accepted).sum())
        print(
            f"{threshold:.2f}  {int(accepted.sum()):3d}  "
            f"{accepted.mean():.0%}  {f1_score(frame['label'], predictions, average='macro'):.3f}  "
            f"{int((~accepted).sum())}  {errors}"
        )


if __name__ == "__main__":
    main()
