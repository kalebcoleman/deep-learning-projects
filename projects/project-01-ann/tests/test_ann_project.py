import torch

from src.loss import MSERegressionLoss
from src.model import (
    LinearRegressionModel,
    SingleHiddenLayerNetwork,
    ThreeHiddenLayerNetwork,
    count_trainable_parameters,
)
from src.train import ExperimentRunner, SeedManager, TrainConfig


def test_parameter_count_matches_closed_form() -> None:
    input_dim = 11
    linear = LinearRegressionModel(input_dim=input_dim)
    one_hidden = SingleHiddenLayerNetwork(input_dim=input_dim, hidden_dim=12)
    three_hidden = ThreeHiddenLayerNetwork(input_dim=input_dim, hidden_dims=(12, 8, 4))

    assert count_trainable_parameters(linear) == 12
    assert count_trainable_parameters(one_hidden) == 157
    assert count_trainable_parameters(three_hidden) == 289


def test_full_batch_training_reduces_loss() -> None:
    SeedManager.set_seed(499)
    features = torch.randn(64, 11)
    target = (features @ torch.randn(11, 1)).squeeze(-1) + 0.25

    runner = ExperimentRunner(loss_fn=MSERegressionLoss())
    result = runner.train_model(
        model=LinearRegressionModel(input_dim=11),
        features=features,
        targets=target,
        config=TrainConfig(learning_rate=0.01, max_epochs=400),
    )

    assert result.loss_history[0] > result.loss_history[-1]
    assert result.final_loss < result.loss_history[0]
