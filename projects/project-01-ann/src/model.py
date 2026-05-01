from __future__ import annotations

import torch
from torch import nn


class FullyConnectedRegressor(nn.Module):
    def __init__(self, input_dim: int, hidden_dims: tuple[int, ...]) -> None:
        super().__init__()
        layers: list[nn.Module] = []
        in_features = input_dim

        for hidden_dim in hidden_dims:
            layers.append(nn.Linear(in_features, hidden_dim))
            layers.append(nn.ReLU())
            in_features = hidden_dim

        layers.append(nn.Linear(in_features, 1))
        self.network = nn.Sequential(*layers)

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        return self.network(features).squeeze(-1)


class LinearRegressionModel(FullyConnectedRegressor):
    def __init__(self, input_dim: int) -> None:
        super().__init__(input_dim=input_dim, hidden_dims=())


class SingleHiddenLayerNetwork(FullyConnectedRegressor):
    def __init__(self, input_dim: int, hidden_dim: int = 12) -> None:
        super().__init__(input_dim=input_dim, hidden_dims=(hidden_dim,))


class ThreeHiddenLayerNetwork(FullyConnectedRegressor):
    def __init__(
        self, input_dim: int, hidden_dims: tuple[int, int, int] = (12, 8, 4)
    ) -> None:
        super().__init__(input_dim=input_dim, hidden_dims=hidden_dims)


def count_trainable_parameters(model: nn.Module) -> int:
    return sum(
        parameter.numel() for parameter in model.parameters() if parameter.requires_grad
    )
