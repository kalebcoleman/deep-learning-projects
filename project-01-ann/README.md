# Project 01: ANN Baseline

PyTorch implementation for MAT499/599 Project 1 (wine quality regression).

## Contents
- `notebooks/Project_1.ipynb`: primary graded notebook submission.
- `src/`: OOP model classes, data loading, loss module, and training runner.
- `tests/`: small regression tests for parameter counts and training behavior.
- `scripts/run.sh`: command-line entrypoint for generating metrics.
- `outputs/`: metrics file plus plots/models folders.

## Run Script
From this folder run:
```
bash scripts/run.sh
```

## Run Notebook
Open `notebooks/Project_1.ipynb` in Jupyter and run all cells top-to-bottom.

If you are enrolled in MAT599, set `CLASS_SEED = 599` in the notebook.

## Tests
Run:
```
pytest -q
```

## Outputs
- `outputs/metrics.json`: summary metrics from script execution.
- `outputs/models/` and `outputs/plots/`: artifact directories.
