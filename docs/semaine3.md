# TP3 : API FastAPI

L'API charge le modèle au démarrage et refuse de démarrer si le fichier Joblib est
absent, afin de rendre une configuration invalide immédiatement visible. Les routes
`/health` et `/predict` sont couvertes par des tests HTTP avec validation Pydantic.

Les données invalides sont refusées en 422, tandis qu'une panne inattendue du modèle
est une erreur serveur 500. La validation Pydantic et le contrôle de texte dans le
modèle sont volontairement redondants : ils protègent respectivement le contrat HTTP
et l'appel direct de la fonction de prédiction.
