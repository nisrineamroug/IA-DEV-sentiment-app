# TP6 : paquet installable

Le paquet `sentiment-app` est déclaré en version 0.6.0 dans `pyproject.toml`. Il
expose la commande `sentiment`, contient le module de prédiction public et peut
être construit en roue avec `python -m build --wheel`.

Le modèle n'est volontairement pas embarqué dans la roue : l'installation reste
légère et l'emplacement du modèle est explicite via `SENTIMENT_MODELE`. Cette
séparation évite de publier un artefact binaire lourd ou dépendant d'une version
particulière de scikit-learn.
