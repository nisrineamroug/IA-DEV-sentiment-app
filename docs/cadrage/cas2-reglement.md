# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)

Permettre aux élèves, aux parents et au personnel de trouver rapidement une réponse fiable à leurs questions sur le règlement intérieur.

## Utilisateur final (obligatoire)

Les élèves et leurs responsables légaux sont les utilisateurs principaux ; la vie scolaire peut aussi utiliser l'outil pour orienter les demandes répétitives.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

(b) Le règlement intérieur et ses annexes existent déjà et permettent de citer le passage utilisé pour chaque réponse, ce qui rend la réponse vérifiable. (d) Une réponse erronée peut induire une sanction injuste ; la réponse doit donc afficher sa source et proposer un transfert à la vie scolaire en cas de doute.

## Données nécessaires et leur origine (obligatoire)

Version validée du règlement intérieur, annexes et procédures publiées par l'établissement, récupérées auprès de la direction puis découpées en passages avec leur titre et leur date de mise à jour. Les versions obsolètes sont archivées et exclues de l'index actif.

## Métrique de succès et seuil d'acceptation (obligatoire)

Exactitude des réponses évaluée sur un jeu de 50 questions représentatives, avec une citation correcte du document dans au moins 90 % des cas et aucune réponse inventée sur les questions testées. Une question sans preuve retrouvée doit être refusée ou transmise à un humain.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une réponse incorrecte peut provoquer une incompréhension du règlement ou une sanction mal appliquée. Chaque réponse affiche le passage source, et les cas sensibles ou ambigus sont validés par la vie scolaire avant toute décision.

## Risques éthiques ou de confidentialité (obligatoire)

Les questions peuvent révéler une situation personnelle ou concerner un mineur : limiter la conservation des échanges, contrôler les accès et informer les utilisateurs du fonctionnement de l'outil. Ne jamais exposer de données personnelles dans les réponses ni utiliser une question individuelle pour entraîner le modèle sans consentement.

## Approche écartée et pourquoi (facultatif)

Les règles métier seules sont écartées car elles ne couvriraient pas les formulations variées des questions ; un modèle génératif seul est écarté car il ne garantirait pas la vérifiabilité des réponses.
