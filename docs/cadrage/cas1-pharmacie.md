# Fiche de cadrage : Ordonnances incomplètes en pharmacie

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Signaler les ordonnances incomplètes avant leur validation par la pharmacie.

## Utilisateur final (obligatoire)

Les pharmaciens et préparateurs vérifient les ordonnances dans leur outil de délivrance.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Les champs obligatoires sont définis par les règles de prescription et chaque alerte doit pouvoir être expliquée par la règle manquante. (d) Une validation à tort peut exposer un patient à une erreur de délivrance ; des règles déterministes et une vérification par un pharmacien sont donc préférables. L'approche ne nécessite pas de données étiquetées (a).

## Données nécessaires et leur origine (obligatoire)

Liste des champs obligatoires validée par le pharmacien, règles internes de contrôle et ordonnance saisie par le professionnel. Les données de santé restent dans le système autorisé et ne sont pas utilisées au-delà du contrôle nécessaire.

## Métrique de succès et seuil d'acceptation (obligatoire)

Sur un jeu de 100 ordonnances annotées par deux pharmaciens, atteindre 100 % de détection des champs obligatoires absents et au moins 99 % de précision des alertes avant mise en production.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une omission non signalée peut entraîner une délivrance incorrecte ; une alerte injustifiée ralentit le travail. Toute ordonnance signalée ou ambiguë est vérifiée par un pharmacien avant validation.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données de santé sensibles : appliquer le contrôle d'accès, chiffrer les échanges, limiter la conservation et journaliser les consultations sans exposer le contenu dans les logs.

## Approche écartée et pourquoi (facultatif)
