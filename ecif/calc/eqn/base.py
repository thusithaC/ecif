"""Base representation of an equation for regression."""

from pydantic import BaseModel, model_validator


class BaseEquation(BaseModel):
    """Base representation of an equation."""

    target: str
    numerical_vars: None | list[str]
    categorical_vars: None | list[str]

    def __repr__(self):
        """String representation of an equation."""
        return self.to_str()

    def to_str(self) -> str:
        """Method to obtain string representation of an equation."""
        eqn = f"{self.target} ~ "
        if self.numerical_vars:
            numerical_part = " + ".join(self.numerical_vars)
        else:
            numerical_part = ""

        if self.categorical_vars:
            categorical_vars = [f"C({var}, Treatment)" for var in self.categorical_vars]
            categorical_part = " + ".join(categorical_vars)
        else:
            categorical_part = ""
        if numerical_part and categorical_part:
            rhs = f"{numerical_part} + {categorical_part}"
        elif numerical_part:
            rhs = numerical_part
        else:
            rhs = categorical_part
        eqn_complete = eqn + rhs
        return eqn_complete

    @model_validator(mode="after")
    def has_one_variable(self):
        """Check one variable is present."""
        if self.numerical_vars or self.categorical_vars:
            return self
        raise ValueError("At least one variable must be present.")
