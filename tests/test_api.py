from fastapi.testclient import TestClient

from api.main import app


def test_health():
    with TestClient(app) as client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_predict_positive():
    with TestClient(app) as client:
        response = client.post("/predict", json={"text": "Livraison rapide, produit conforme, très satisfait"})
    assert response.status_code == 200
    assert response.json()["label"] == "POSITIVE"


def test_predict_negative():
    with TestClient(app) as client:
        response = client.post("/predict", json={"text": "Produit cassé et service injoignable, à fuir"})
    assert response.status_code == 200
    assert response.json()["label"] == "NEGATIVE"


def test_invalid_payloads():
    with TestClient(app) as client:
        assert client.post("/predict", json={"text": ""}).status_code == 422
        assert client.post("/predict", json={}).status_code == 422
        assert client.post("/predict", json={"text": 42}).status_code == 422
        assert client.post("/predict", json={"text": "   "}).status_code == 422


def test_response_contract():
    with TestClient(app) as client:
        payload = client.post("/predict", json={"text": "xqzvb wlkptr grombu"}).json()
    assert set(payload) == {"label", "score", "text", "abstained"}
    assert payload["label"] == "INDETERMINE"
