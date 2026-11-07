"""Streamlit interface for single reviews and CSV batches."""
from __future__ import annotations

import os

import pandas as pd
import requests
import streamlit as st

API_URL = os.environ.get("SENTIMENT_API_URL", "http://127.0.0.1:8000")


def call_api(text: str) -> dict[str, object]:
    response = requests.post(f"{API_URL}/predict", json={"text": text}, timeout=10)
    if response.status_code == 422:
        detail = response.json().get("detail", "Texte refusé")
        raise ValueError(f"Texte refusé : {detail}")
    response.raise_for_status()
    return response.json()


def render_result(result: dict[str, object]) -> None:
    label = str(result["label"])
    score = float(result["score"])
    if label == "INDETERMINE":
        st.warning(f"Je ne sais pas : à faire vérifier par un humain ({score:.0%})")
    else:
        st.success(f"Avis {'positif' if label == 'POSITIVE' else 'négatif'} : {score:.0%}")
    st.caption(f"Confiance : {score:.1%}")


def main() -> None:
    st.set_page_config(page_title="Analyse de sentiment", page_icon="💬")
    st.title("Analyse de sentiment")
    try:
        health = requests.get(f"{API_URL}/health", timeout=3).json()
        st.info(f"API prête : {health['model']}")
    except requests.RequestException:
        st.error("API injoignable : lancez d'abord uvicorn api.main:app")
    tab_single, tab_file = st.tabs(["Un avis", "Un fichier d'avis"])
    with tab_single:
        text = st.text_area("Votre avis", placeholder="Écrivez un avis...")
        if st.button("Analyser"):
            try:
                render_result(call_api(text))
            except (ValueError, requests.RequestException) as exc:
                st.warning(str(exc))
    with tab_file:
        uploaded = st.file_uploader("CSV contenant une colonne review ou text", type="csv")
        if uploaded is not None:
            frame = pd.read_csv(uploaded)
            column = "review" if "review" in frame.columns else "text"
            results = []
            for text_value in frame[column].fillna(""):
                try:
                    result = call_api(str(text_value))
                except (ValueError, requests.RequestException) as exc:
                    result = {"label": "ERREUR", "score": 0.0, "error": str(exc)}
                results.append(result)
            output = frame.copy()
            output["label"] = [result["label"] for result in results]
            output["score"] = [result["score"] for result in results]
            st.dataframe(output)
            st.write(output["label"].value_counts().to_dict())
            st.download_button(
                "Télécharger les résultats",
                output.to_csv(index=False).encode(),
                "resultats.csv",
                "text/csv",
            )


if __name__ == "__main__":
    main()
