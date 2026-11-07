# TP2 : modèle de sentiment

Le jeu de démonstration contient 290 avis synthétiques équilibrés entre les classes
`positive` et `negative`. Le pipeline TF-IDF et régression logistique est reproductible
avec `random_state=42` et atteint un F1 macro de 1.000 sur le test local ; `metrics.json`
est versionné tandis que le fichier Joblib est régénéré.

Les avis courts ou ambigus restent les plus fragiles pour un modèle de sac de mots :
les termes positifs et négatifs peuvent se neutraliser dans une même phrase. Une
amélioration consisterait à ajouter des exemples annotés variés, des n-grammes plus
riches et une revue humaine des prédictions de confiance faible.
