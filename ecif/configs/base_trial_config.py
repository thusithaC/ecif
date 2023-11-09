"""Config object for a Trial."""
from enum import Enum
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationError, model_validator
from pydantic_yaml import parse_yaml_file_as


class CalculationMethod(Enum):
    """Enumeration for calculation method."""

    CLASSICAL_REGRESSION = "classical-regression"
    CLASSICAL_DID_REGRESSION = "classical-did-regression"


class DataModel(BaseModel):
    """Data setup for the trial."""

    model_config = ConfigDict(frozen=True, from_attributes=True)

    target_column: str
    treatment_column: str
    control_variable_columns: None | list[str]


class CalculationModel(BaseModel):
    """Calculation model for the trial."""

    model_config = ConfigDict(frozen=True, from_attributes=True)

    method: CalculationMethod
    estimate_intervals: bool
    interval_level: None | float = 0.95

    @model_validator(mode="after")
    def is_interval_defined(self):
        """Validate if interval level is defined if estimate_intervals."""
        if self.estimate_intervals is True:
            if self.interval_level is None:
                raise ValidationError(
                    "interval_level must be defined if estimate_intervals is True"
                )
        return self


class BaseTrialConfig(BaseModel):
    """General configuration for a trial."""

    trial_name: str
    data: DataModel
    calculation_model: CalculationModel

    @classmethod
    def from_yaml(cls, file: str | Path) -> "BaseTrialConfig":
        """Create object from yaml file."""
        return parse_yaml_file_as(cls, file)
