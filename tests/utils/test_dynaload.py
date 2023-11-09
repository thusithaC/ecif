"""Test dynamic loading of classes."""
from ecif.utils.dynaload import str_to_class
from ecif.configs.base_trial_config import BaseTrialConfig
from ecif.exceptions.core_exceptions import ClassNotFoundException
import pytest


def test_can_load_class():
    """Successfully loads a class."""
    config_class_ = str_to_class("ecif.configs.base_trial_config.BaseTrialConfig")
    assert config_class_ == BaseTrialConfig


@pytest.mark.parametrize("class_with_module", ["fake.BaseTrialConfig", "BaseTrialConfig", "ecif.BaseTrialConfig", "ecif.configs.base_trial_config.BaseTrialConfigs"])
def test_throws_exception(class_with_module):
    """Successfully loads a class."""
    with pytest.raises(ClassNotFoundException):
        _ = str_to_class(class_with_module)
