# Deep Learning Projects (Spring 2026)

Course projects covering core deep learning models and workflows. Each project is self-contained with its own `src/`, `notebooks/`, and `scripts/`.

## Structure
- `project-01-ann/`: Fully connected neural network (ANN) baseline.
- `project-02-hpo/`: Hyperparameter optimization and search.
- `project-03-cnn/`: Convolutional neural networks and filter visualization.
- `project-04-rnn/`: Sequence modeling with RNNs.
- `shared/`: Reusable helpers and utilities across projects.
- `environment/`: Conda environment used for development.

## Setup
Create the conda environment:
```
conda env create -f environment/environment.yml
conda activate deep-learning
```

## Running a project
Each project has a `README.md` with instructions and a `scripts/` folder with the primary run command.

## Notes
Large files (datasets, model checkpoints, results) are intentionally ignored via `.gitignore`.
