"""Generate the deterministic review dataset used by local development."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "demo_reviews.csv"

POSITIVE = [
    "Service impeccable et livraison rapide, je recommande.",
    "Produit conforme, qualité excellente et expérience agréable.",
    "Interface simple, efficace et très facile à utiliser.",
    "Très satisfait de cette commande et du support.",
]
NEGATIVE = [
    "Produit cassé à l'arrivée et service client injoignable.",
    "Commande jamais reçue, remboursement toujours en attente.",
    "Application qui plante et expérience vraiment décevante.",
    "Qualité médiocre, livraison tardive et support inutile.",
]
MIXED = [
    "Le produit est joli mais la livraison est très lente.",
    "Service agréable, toutefois la qualité reste décevante.",
    "Prix correct mais application compliquée et instable.",
    "Bonne idée, mais le résultat est loin d'être parfait.",
]
NEUTRAL = [
    "Le colis est arrivé mardi dans un emballage standard.",
    "J'ai utilisé le service pendant deux semaines.",
    "La commande contient un produit de couleur bleue.",
]


def build_reviews() -> list[dict[str, str]]:
    reviews: list[dict[str, str]] = []
    for index in range(145):
        reviews.append({"review": POSITIVE[index % len(POSITIVE)], "label": "positive"})
        reviews.append({"review": NEGATIVE[index % len(NEGATIVE)], "label": "negative"})
    return reviews


def main() -> None:
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows = build_reviews()
    with DATA_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["review", "label"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} avis écrits, 145 positifs et 145 négatifs")
    print("Jeu de démonstration reproductible généré dans data/demo_reviews.csv")


if __name__ == "__main__":
    main()
