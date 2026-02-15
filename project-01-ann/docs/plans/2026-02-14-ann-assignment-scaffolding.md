# Design: PyTorch ANN Assignment Scaffolding

**Date**: 2026-02-14
**Project**: Project 01: ANN Baseline

## 1. Overview
The goal is to transition the current repository from a set of empty placeholders into a functional "Hybrid Module" structure for a PyTorch ANN assignment. This structure balances clean software engineering (modular `src/`) with the rapid iteration required by deep learning assignments (interactive `notebooks/`).

## 2. Architecture: Hybrid Module
The core logic resides in Python modules, while the experimentation and visualization happen in Jupyter notebooks.

### 2.1 Directory Map & File Roles

#### `src/` (The Engine)
- **`model.py`**: Contains `nn.Module` definitions. Recommended naming: `SimpleANN` or `BaselineMLP`.
- **`data.py`**: Contains `torch.utils.data.Dataset` and `DataLoader` logic. Includes a `get_dataloaders()` helper function.
- **`train.py`**: Contains the training loop logic (`train_one_epoch`, `validate`).
- **`loss.py`**: Wrapper for loss functions (e.g., CrossEntropy, MSE).

#### `notebooks/` (The Dashboard)
- **`ann_experiments.ipynb`**: Imports from `src`, sets hyperparameters, executes the training loop, and generates all required assignment plots.

#### `outputs/` (The Artifacts)
- **`models/`**: (New) Directory for `.pth` or `.pt` model weights.
- **`plots/`**: (New) Directory for saving loss curves, accuracy plots, and confusion matrices.
- **`metrics.json`**: A structured log of training history (epoch, loss, accuracy).

#### `scripts/` (The Entrypoints)
- **`run.sh`**: A simple bash script to trigger a CLI-based training run (`python -m src.train`).

## 3. Implementation Plan
1. **Scaffold `src/`**: Populate `model.py`, `data.py`, and `train.py` with standard PyTorch boilerplate.
2. **Setup `notebooks/`**: Configure `ann_experiments.ipynb` to import and run the `src` modules.
3. **Initialize `outputs/`**: Create the `models/` and `plots/` subdirectories.
4. **Define `scripts/run.sh`**: Update the placeholder to provide a quick command-line training option.

## 4. Naming Conventions
- Classes: PascalCase (e.g., `ANNModel`, `SyntheticDataset`)
- Functions/Variables: snake_case (e.g., `train_one_epoch`, `learning_rate`)
- Checkpoints: `ann_baseline_{timestamp}.pth`
