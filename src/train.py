"""Train and persist the sentiment classifier."""
from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "demo_reviews.csv"
MODEL_PATH = ROOT / "models" / "sentiment.joblib"
METRICS_PATH = ROOT / "models" / "metrics.json"


def load_reviews(use_allocine: bool = False) -> tuple[pd.DataFrame, str]:
    if use_allocine:
        try:
            from datasets import load_dataset  # type: ignore[import-not-found]

            dataset = load_dataset("allocine", split="train")
            frame = pd.DataFrame(dataset).rename(columns={"text": "review", "label": "label"})
            frame["label"] = frame["label"].map({0: "negative", 1: "positive"})
            return frame[["review", "label"]], "allocine"
        except Exception as exc:
            print(f"Allociné indisponible ({exc}); utilisation du jeu de démonstration.")
    if not DATA_PATH.exists():
        from make_demo import main as make_demo

        make_demo()
    return pd.read_csv(DATA_PATH), "demo"


def train(use_allocine: bool = False) -> dict[str, object]:
    frame, source = load_reviews(use_allocine)
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        frame["review"],
        frame["label"],
        test_size=0.2,
        random_state=42,
        stratify=frame["label"],
    )
    pipeline = Pipeline(
        [
            ("tfidf", TfidfVectorizer(ngram_range=(1, 2), lowercase=True)),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )
    pipeline.fit(train_texts, train_labels)
    predictions = pipeline.predict(test_texts)
    score = float(f1_score(test_labels, predictions, average="macro"))
    vocabulary = len(pipeline.named_steps["tfidf"].vocabulary_)
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    metrics = {
        "source": source,
        "samples": int(len(frame)),
        "test_samples": int(len(test_texts)),
        "vocabulary": vocabulary,
        "f1_macro": round(score, 4),
        "created_at": datetime.now(UTC).isoformat(),
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Source : {source}, {len(frame)} avis")
    print(f"{len(train_texts)} avis d'entraînement, {len(test_texts)} de test")
    print(f"Vocabulaire : {vocabulary} termes")
    print(f"F1 macro sur le jeu de test : {score:.3f}")
    print(f"Modèle : {MODEL_PATH.relative_to(ROOT)}")
    print(f"Métriques : {METRICS_PATH.relative_to(ROOT)}")
    return metrics


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--allocine", action="store_true", help="Use Allociné when available.")
    args = parser.parse_args()
    train(args.allocine)


if __name__ == "__main__":
    main()
