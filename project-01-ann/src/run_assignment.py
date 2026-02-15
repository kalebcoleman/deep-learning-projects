from __future__ import annotations

import json
from pathlib import Path

from src.data import WineQualityData
from src.loss import MSERegressionLoss
from src.model import (
    LinearRegressionModel,
    SingleHiddenLayerNetwork,
    ThreeHiddenLayerNetwork,
)
from src.train import ExperimentRunner, SeedManager, TrainConfig


def main() -> None:
    seed = 499
    SeedManager.set_seed(seed)

    dataset = WineQualityData()
    features, targets = dataset.load_tensors(standardize=True)

    runner = ExperimentRunner(loss_fn=MSERegressionLoss())
    config = TrainConfig(learning_rate=0.01, max_epochs=20000)

    model_factories = {
        "Linear": lambda: LinearRegressionModel(input_dim=features.shape[1]),
        "SingleHidden12": lambda: SingleHiddenLayerNetwork(
            input_dim=features.shape[1], hidden_dim=12
        ),
        "ThreeHidden12_8_4": lambda: ThreeHiddenLayerNetwork(
            input_dim=features.shape[1], hidden_dims=(12, 8, 4)
        ),
    }

    results = runner.run_model_collection(
        model_factories=model_factories,
        features=features,
        targets=targets,
        config=config,
    )

    payload = {
        "seed": seed,
        "results": {
            name: {
                "model_name": result.model_name,
                "learning_rate": result.learning_rate,
                "epochs_run": result.epochs_run,
                "final_loss": result.final_loss,
                "converged": result.converged,
                "loss_history_head": result.loss_history[:5],
                "loss_history_tail": result.loss_history[-5:],
            }
            for name, result in results.items()
        },
    }
    output_path = Path("outputs/metrics.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
