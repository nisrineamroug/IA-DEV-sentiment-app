from fastapi.testclient import TestClient

from api.main import app


def test_text_length_contract():
    with TestClient(app) as client:
        assert client.post("/predict", json={"text": "a" * 2001}).status_code == 422


def test_extra_fields_are_rejected():
    with TestClient(app) as client:
        assert client.post("/predict", json={"text": "good", "extra": 1}).status_code == 422
