# Project 01: ANN Wine Quality

Notebook-first PyTorch project for MAT499 Project 1. The primary artifact is `notebooks/01_ann-wine-quality.ipynb`.

## Contents

- `notebooks/01_ann-wine-quality.ipynb`: graded notebook for wine-quality regression.
- `src/`: small support package imported by the notebook (`data.py`, `model.py`, `loss.py`, `train.py`).
- `tests/`: regression tests for model parameter counts and training behavior.
- `data/README.md`: notes on the remote wine-quality dataset.

## Run Notebook

From this folder or the repository root:

```bash
jupyter lab notebooks/01_ann-wine-quality.ipynb
```

Run all cells top-to-bottom.

## Tests

From this folder:

```bash
pytest -q
```

Legacy script entrypoints were moved to `archive/legacy-code/project-01-ann-scripts/`.
