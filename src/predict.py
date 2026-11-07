"""Compatibility module for the TP2 command."""
from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Prediction:
    label: str
    score: float
    abstained: bool


def load_model(path: Path | None = None) -> Any:
    model_path = path or Path(os.environ.get("SENTIMENT_MODELE", ROOT / "models" / "sentiment.joblib"))
    if not model_path.exists():
        raise FileNotFoundError(f"{model_path} absent : lancez python src/train.py")
    return joblib.load(model_path)


def predict(text: str, model: Any = None, threshold: float = 0.6) -> Prediction:
    if not text.strip():
        raise ValueError("texte vide")
    classifier = model or load_model()
    probabilities = classifier.predict_proba([text])[0]
    index = int(probabilities.argmax())
    score = float(probabilities[index])
    return Prediction(str(classifier.classes_[index]).upper(), score, score < threshold)

__all__ = ["Prediction", "load_model", "predict"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    result = predict(args.text)
    label = "INDETERMINE" if result.abstained else result.label
    print(f"{label} (confiance {result.score:.0%})")


if __name__ == "__main__":
    main()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    result = predict(args.text)
    label = "INDETERMINE" if result.abstained else result.label
    print(f"{label} (confiance {result.score:.0%})")


if __name__ == "__main__":
    main()
