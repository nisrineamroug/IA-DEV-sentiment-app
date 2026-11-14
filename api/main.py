"""HTTP API for sentiment predictions."""
from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException, Request

from .model import load_model, predict
from .schemas import PredictRequest, PredictResponse

MODEL_NAME = "tfidf-logreg (TP2, models/sentiment.joblib)"


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncIterator[None]:
    classifier = load_model()
    application.state.classifier = classifier
    application.state.loaded_classifier = classifier
    yield


app = FastAPI(title="Sentiment API", version="0.6.0", lifespan=lifespan)


def _classifier(request: Request) -> Any:
    state = request.app.state
    classifier = getattr(state, "classifier", getattr(state, "loaded_classifier", None))
    if classifier is None:
        raise HTTPException(status_code=503, detail="Modèle non chargé")
    return classifier


@app.get("/health")
def health(request: Request) -> dict[str, str]:
    _classifier(request)
    return {"status": "OK", "model": MODEL_NAME}


@app.post("/predict", response_model=PredictResponse)
def prediction(payload: PredictRequest, request: Request) -> PredictResponse:
    classifier = _classifier(request)
    try:
        result = predict(payload.text, model=classifier)
    except ValueError as exc:
        detail = [{"loc": ["body", "text"], "msg": str(exc), "type": "value_error"}]
        raise HTTPException(status_code=422, detail=detail) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Erreur interne du modèle") from exc
    label = "INDETERMINE" if result.abstained else result.label
    return PredictResponse(label=label, score=result.score, text=payload.text[:100], abstained=result.abstained)
