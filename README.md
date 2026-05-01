# Deep Learning Coursework Projects

This repository is a notebook-first collection of deep learning coursework and applied projects. The main artifacts are Jupyter notebooks: class exercises live in `notebooks/`, and larger assignments live in `projects/project-XX-name/notebooks/`.

The layout is intentionally simple for review by recruiters, research labs, and course staff. Legacy scripts, empty placeholders, runtime state, and old shared-code scaffolding are preserved under `archive/` instead of being deleted.

## Structure

- `notebooks/`: numbered coursework notebooks covering gradient descent, classification, regularization, optimization, and CNN basics.
- `projects/project-01-ann/`: wine-quality regression with fully connected neural networks.
- `projects/project-02-hpo/`: hyperparameter optimization experiments.
- `projects/project-03-cnn/`: Fashion-MNIST CNN classification.
- `projects/project-04-wildfire-smoke/`: wildfire smoke bounding-box prediction with a pretrained CNN.
- `docs/notebook-index.md`: notebook index with topic, model, and dataset summaries.
- `archive/`: legacy code, empty placeholders, checkpoints, and tool/runtime state kept out of the active learning path.
- `environment.yml`: Conda environment for running notebooks.

## Setup

```bash
conda env create -f environment.yml
conda activate deep-learning
python -m ipykernel install --user --name deep-learning --display-name "Python (deep-learning)"
```

## How To Use

Start with `docs/notebook-index.md`, then open the notebook that matches the topic or project you want to review.

For coursework notebooks:

```bash
jupyter lab notebooks/
```

For major projects:

```bash
jupyter lab projects/project-01-ann/notebooks/
```

Project 1 keeps a small `src/` package because its graded notebook imports those model, data, loss, and training classes directly. Other empty script/module scaffolds were archived.
