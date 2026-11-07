# Fiche de cadrage : Priorisation des avis négatifs

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Classer les avis clients afin de faire remonter rapidement les retours négatifs à l'équipe support.

## Utilisateur final (obligatoire)

Les équipes support, qualité et expérience client consultent la file priorisée pour traiter les problèmes récurrents.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(a) Des avis historiques peuvent être étiquetés positifs ou négatifs par l'équipe qualité, ce qui permet d'entraîner et d'évaluer un classifieur. (c) Le volume est élevé et un modèle léger réduit le coût par requête. (d) Une erreur de classement ne bloque pas une commande mais peut retarder un incident ; les avis à confiance faible sont donc revus par un humain.

## Données nécessaires et leur origine (obligatoire)

Avis clients anonymisés issus de la base de support, avec une étiquette positive ou négative validée par l'équipe qualité. Les identifiants, coordonnées et autres données personnelles sont supprimés avant l'entraînement.

## Métrique de succès et seuil d'acceptation (obligatoire)

Mesurer le rappel de la classe négative et le taux de faux négatifs sur un jeu de test séparé ; accepter le modèle avec au moins 90 % de rappel négatif et moins de 5 % de faux négatifs.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis négatif mal classé peut retarder la résolution d'un problème client, tandis qu'un avis positif mal classé consomme du temps de revue. Les prédictions peu confiantes et les échantillons de contrôle sont vérifiés par l'équipe support.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des noms, coordonnées ou informations sensibles : anonymiser les données, restreindre les accès, documenter les biais de langue et de registre, et permettre une correction humaine du classement.

## Approche écartée et pourquoi (facultatif)

Le modèle génératif seul est écarté car son coût et sa variabilité sont inutiles pour une classification binaire vérifiable ; le RAG n'est pas nécessaire quand la décision porte sur le texte de l'avis lui-même.

## Approche écartée et pourquoi (facultatif)
