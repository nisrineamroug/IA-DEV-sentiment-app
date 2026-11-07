# TP4 : tests et qualité

Les tests couvrent les limites du contrat (`texte vide`, espaces, longueur maximale,
champs supplémentaires), l'intégration HTTP et l'abstention. Le seuil local de 0.60
permet d'afficher `INDETERMINE` lorsque la confiance est insuffisante plutôt que de
forcer un verdict.

Ruff et mypy sont exécutés localement et dans la CI. Le crochet pre-commit applique
Ruff avant chaque commit afin de détecter tôt les imports inutilisés et les erreurs
de style.
