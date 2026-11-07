"""Prediction API independent of the repository working directory."""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib


@dataclass(frozen=True)
class Prediction:
    label: str
    score: float
    abstained: bool


def load_model(path: str | Path | None = None) -> Any:
    configured = path or os.environ.get("SENTIMENT_MODELE")
    if configured is None:
        configured = Path(__file__).resolve().parents[1] / "models" / "sentiment.joblib"
    model_path = Path(configured)
    if not model_path.exists():
        raise FileNotFoundError(f"{model_path} absent : définissez SENTIMENT_MODELE ou lancez src/train.py")
    return joblib.load(model_path)


def predict(text: str, model: Any = None, threshold: float = 0.6) -> Prediction:
    if not text.strip():
        raise ValueError("texte vide")
    classifier = model or load_model()
    probabilities = classifier.predict_proba([text])[0]
    index = int(probabilities.argmax())
    score = float(probabilities[index])
    return Prediction(str(classifier.classes_[index]).upper(), score, score < threshold)
