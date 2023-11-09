"""Test creating a configuration object."""
from ecif.configs.base_trial_config import BaseTrialConfig, CalculationModel, DataModel


def test_create_config(test_configs):
    """Test creating a config."""
    config_file = test_configs["cr-online-classroom"]
    config = BaseTrialConfig.from_yaml(config_file)
    assert config.trial_name == "Test Classical Regression with online_classroom data"
    assert isinstance(config.calculation_model, CalculationModel)
    assert isinstance(config.data, DataModel)
