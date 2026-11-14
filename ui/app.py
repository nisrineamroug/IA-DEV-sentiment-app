"""Interface Streamlit pour les avis unitaires et les lots CSV."""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import streamlit as st

if not __package__:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from ui import client


def call_api(text: str) -> dict[str, object]:
    """Compatibilité avec l'ancien point d'entrée de l'interface."""
    with client.creer_session() as session:
        result = client.predire(session, text)
    if not result.ok:
        raise ValueError(result.message)
    return {"label": result.label, "score": result.score}


def main() -> None:
    st.set_page_config(page_title="Analyse de sentiment")
    st.title("Analyse de sentiment")
    session = client.creer_session()
    health = client.sante(session)
    if health.ok:
        st.caption(f"API prête : {health.message}")
    else:
        st.error(health.message)

    tab_single, tab_file = st.tabs(["Un avis", "Un fichier d'avis"])
    with tab_single:
        text = st.text_area("Votre avis", placeholder="Écrivez un avis...")
        if st.button("Analyser"):
            result = client.predire(session, text)
            if not result.ok:
                st.warning(result.message)
            elif result.label == "INDETERMINE":
                st.metric("Je ne sais pas : à faire vérifier par un humain", f"{result.score:.0%}")
                st.info("Confiance sous le seuil d'abstention.")
            else:
                st.metric(client.VERDICTS[result.label or ""], f"{result.score:.0%}")

    with tab_file:
        uploaded = st.file_uploader("CSV contenant une colonne review ou text", type="csv")
        if uploaded is not None:
            frame = pd.read_csv(uploaded)
            column = "review" if "review" in frame.columns else "text"
            results = client.predire_lot(session, [str(value) for value in frame[column].fillna("")])
            output = frame.copy()
            output["label"] = [result.label or "ERREUR" for result in results]
            output["score"] = [result.score or 0.0 for result in results]
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
