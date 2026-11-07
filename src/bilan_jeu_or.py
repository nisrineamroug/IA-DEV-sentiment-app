"""Run a small manually curated evaluation set."""
from __future__ import annotations

from predict import predict

GOLD = [
    ("Livraison rapide et produit parfait", "POSITIVE"),
    ("Service horrible, commande perdue", "NEGATIVE"),
    ("Je recommande vivement cette expérience", "POSITIVE"),
    ("Produit inutilisable et très déçu", "NEGATIVE"),
] * 5


def main() -> None:
    results = [predict(text) for text, _ in GOLD]
    abstentions = sum(result.abstained for result in results)
    errors = sum(not result.abstained and result.label != expected for result, (_, expected) in zip(results, GOLD))
    print(f"Jeu d'or : {len(GOLD)} avis, {abstentions} abstention(s), {errors} erreur(s)")


if __name__ == "__main__":
    main()
