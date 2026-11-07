from __future__ import annotations

import json

import pytest

from src.predict import predict
from src.train import METRICS_PATH


def test_metrics_exist_and_meet_threshold():
    assert METRICS_PATH.exists()
    metrics = json.loads(METRICS_PATH.read_text(encoding="utf-8"))
    assert metrics["f1_macro"] >= 0.85


@pytest.mark.skipif(not __import__("pathlib").Path("models/sentiment.joblib").exists(), reason="model not trained")
def test_prediction_labels():
    assert predict("Service impeccable et livraison rapide").label == "POSITIVE"
    assert predict("Produit cassé et service horrible").label == "NEGATIVE"
