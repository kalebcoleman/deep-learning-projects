from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import torch


@dataclass(frozen=True)
class WineQualityData:
    csv_source: str = "https://raw.githubusercontent.com/benjaminmlucas/MAT499/refs/heads/main/module_1/winequality.csv"
    target_column: str = "quality"

    def load_dataframe(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_source)

    def load_tensors(
        self, standardize: bool = True
    ) -> tuple[torch.Tensor, torch.Tensor]:
        frame = self.load_dataframe()
        features = frame.drop(columns=[self.target_column]).to_numpy(dtype=np.float32)
        targets = frame[self.target_column].to_numpy(dtype=np.float32)

        if standardize:
            mean = features.mean(axis=0, keepdims=True)
            std = features.std(axis=0, keepdims=True)
            std[std == 0.0] = 1.0
            features = (features - mean) / std

        feature_tensor = torch.tensor(features.tolist(), dtype=torch.float32)
        target_tensor = torch.tensor(targets.tolist(), dtype=torch.float32)
        return feature_tensor, target_tensor

    def split_half(
        self,
        features: torch.Tensor,
        targets: torch.Tensor,
        seed: int,
    ) -> tuple[tuple[torch.Tensor, torch.Tensor], tuple[torch.Tensor, torch.Tensor]]:
        generator = torch.Generator().manual_seed(seed)
        indices = torch.randperm(features.shape[0], generator=generator)
        midpoint = features.shape[0] // 2
        first_idx = indices[:midpoint]
        second_idx = indices[midpoint:]
        return (
            features[first_idx],
            targets[first_idx],
        ), (
            features[second_idx],
            targets[second_idx],
        )
