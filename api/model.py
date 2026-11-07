"""Application-level model adapter."""
from sentiment_app.predict import Prediction, load_model, predict

__all__ = ["Prediction", "load_model", "predict"]
