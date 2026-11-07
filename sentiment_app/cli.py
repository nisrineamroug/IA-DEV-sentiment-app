"""Command-line entry point for the packaged application."""
from __future__ import annotations

import argparse

from . import __version__
from .predict import predict


def main() -> None:
    parser = argparse.ArgumentParser(prog="sentiment")
    parser.add_argument("--version", action="version", version=f"sentiment-app {__version__}")
    subparsers = parser.add_subparsers(dest="command", required=True)
    predict_parser = subparsers.add_parser("predict")
    predict_parser.add_argument("text")
    subparsers.add_parser("serve")
    args = parser.parse_args()
    if args.command == "predict":
        result = predict(args.text)
        label = "INDETERMINE" if result.abstained else result.label
        print(f"{label} (confiance {result.score:.0%})")
    else:
        import uvicorn

        uvicorn.run("api.main:app", host="127.0.0.1", port=8000)
