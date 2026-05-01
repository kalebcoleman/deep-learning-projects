from __future__ import annotations

import random
from dataclasses import asdict, dataclass
from typing import Callable
import math

import numpy as np
import torch
from torch import nn


@dataclass(frozen=True)
class TrainConfig:
    learning_rate: float = 0.01
    max_epochs: int = 20000
    convergence_window: int = 50
    convergence_decimals: int = 4


@dataclass(frozen=True)
class TrainingResult:
    model_name: str
    learning_rate: float
    epochs_run: int
    final_loss: float
    converged: bool
    loss_history: list[float]

    def to_dict(self) -> dict[str, float | int | bool | str | list[float]]:
        return asdict(self)


class SeedManager:
    @staticmethod
    def set_seed(seed: int) -> None:
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)


class ExperimentRunner:
    def __init__(self, loss_fn: nn.Module) -> None:
        self.loss_fn = loss_fn

    @staticmethod
    def has_converged(loss_history: list[float], window: int, decimals: int) -> bool:
        if len(loss_history) < window:
            return False
        if not all(math.isfinite(value) for value in loss_history[-window:]):
            return False
        rounded = [round(value, decimals) for value in loss_history[-window:]]
        return len(set(rounded)) == 1

    def train_model(
        self,
        model: nn.Module,
        features: torch.Tensor,
        targets: torch.Tensor,
        config: TrainConfig,
        model_name: str | None = None,
    ) -> TrainingResult:
        optimizer = torch.optim.SGD(model.parameters(), lr=config.learning_rate)
        loss_history: list[float] = []
        converged = False

        model.train()
        for epoch in range(1, config.max_epochs + 1):
            optimizer.zero_grad(set_to_none=True)
            prediction = model(features)
            loss = self.loss_fn(prediction, targets)
            loss.backward()
            optimizer.step()

            current_loss = float(loss.item())
            loss_history.append(current_loss)

            if self.has_converged(
                loss_history=loss_history,
                window=config.convergence_window,
                decimals=config.convergence_decimals,
            ):
                converged = True
                break

        return TrainingResult(
            model_name=model_name or model.__class__.__name__,
            learning_rate=config.learning_rate,
            epochs_run=len(loss_history),
            final_loss=loss_history[-1],
            converged=converged,
            loss_history=loss_history,
        )

    def run_model_collection(
        self,
        model_factories: dict[str, Callable[[], nn.Module]],
        features: torch.Tensor,
        targets: torch.Tensor,
        config: TrainConfig,
    ) -> dict[str, TrainingResult]:
        results: dict[str, TrainingResult] = {}
        for name, factory in model_factories.items():
            model = factory()
            results[name] = self.train_model(
                model=model,
                features=features,
                targets=targets,
                config=config,
                model_name=name,
            )
        return results
