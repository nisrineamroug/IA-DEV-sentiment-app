# sentiment-app : dépôt individuel

Application individuelle de Nisrine Amroug pour le cours *Développement et déploiement d'applications intelligentes*.
Le projet couvre les TP1 à TP6 : modèle reproductible, API FastAPI, tests de qualité,
interface Streamlit et paquet Python installable.

## Installation (3 commandes)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell : .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Vérifier son installation

```bash
python scripts/check_setup.py    # diagnostic lisible : versions, dossiers, Git
pytest -q                        # mêmes vérifications sous forme de tests
```

Entraîner le modèle local :

```bash
python src/make_demo.py
python src/train.py
```

Lancer l'API et l'interface :

```bash
uvicorn api.main:app
streamlit run ui/app.py
```

Construire le paquet :

```bash
python -m build --wheel
```

La démarche complète de test, étape par étape, est dans `TESTS.md`.

## Structure

```text
sentiment-app/
├── README.md
├── TP1-ENONCE.md    # énoncé du TP de la semaine 1
├── TESTS.md         # démarche à suivre pour le test
├── requirements.txt
├── .gitignore
├── data/            # jeux de données (versionnés par DVC à partir de la semaine 7)
├── models/          # modèles entraînés (jamais dans Git)
├── app/             # API FastAPI (semaine 3)
├── ui/              # Streamlit (semaine 5)
├── tests/           # pytest (semaine 1 : tests d'environnement)
├── scripts/         # utilitaires (check_setup, nouveau cas de cadrage)
└── docs/cadrage/    # fiches de cadrage du TP1
```

## Étudiante

| Nom | Identifiant GitHub | Dépôt |
| --- | --- | --- |
| Nisrine Amroug | [@nisrineamroug](https://github.com/nisrineamroug) | [IA-DEV-sentiment-app](https://github.com/nisrineamroug/IA-DEV-sentiment-app) |

## Journal et guide

Le journal individuel est dans [`docs/journal-tp1-tp6.md`](docs/journal-tp1-tp6.md). Le guide de rattrapage est dans [`docs/guide-rattrapage-tp1-tp5.md`](docs/guide-rattrapage-tp1-tp5.md).
