"""Config object for a Trial."""
from pydantic import BaseModel, ValidationError, model_validator
from enum import Enum


class CalculationMethod(Enum):
    CLASSICAL_DID_REGRESSION = "classical-did-regression"


class DataModel(BaseModel):
    """Data setup for the trial."""
    target_column: str
    treatment_column: str
    control_variable_columns: None | list[str]


class CalculationModel(BaseModel):
    """Calculation model for the trial."""
    method: CalculationMethod
    equation: str
    estimate_intervals: bool
    interval_level: None | float = 0.95

    @model_validator(mode="after")
    def is_interval_defined(self):
        if self.estimate_intervals is True:
            if self.interval_level is None:
                raise ValidationError("interval_level must be defined if estimate_intervals is True")
        return self


class BaseTrialConfig(BaseModel):
    """General configuration for a trial."""
    trial_name: str
    data: DataModel
    calculation_model: CalculationModel





