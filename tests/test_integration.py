from fastapi.testclient import TestClient

from api.main import app


def test_api_end_to_end():
    with TestClient(app) as client:
        health = client.get("/health")
        prediction = client.post("/predict", json={"text": "Service impeccable et livraison rapide"})
    assert health.status_code == 200
    assert prediction.status_code == 200
    assert prediction.json()["score"] >= 0.5
