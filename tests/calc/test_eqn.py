"""Tests for equation reporesentations."""
import pytest
from pydantic import ValidationError

from ecif.calc.eqn.base import BaseEquation


@pytest.mark.parametrize(
    "obj,expected",
    [
        ({"target": "score", "numerical_vars": ["age"], "categorical_vars": None}, "score ~ age"),
        (
            {"target": "score", "numerical_vars": ["age", "gender"], "categorical_vars": None},
            "score ~ age + gender",
        ),
        (
            {"target": "score", "numerical_vars": [], "categorical_vars": ["school_type"]},
            "score ~ C(school_type, Treatment)",
        ),
        (
            {"target": "score", "numerical_vars": ["age"], "categorical_vars": ["school_type"]},
            "score ~ age + C(school_type, Treatment)",
        ),
    ],
)
def test_base_eqn(obj, expected):
    """Test the base representation of equations."""
    eqn = BaseEquation.model_validate(obj)
    assert eqn.to_str() == expected


@pytest.mark.parametrize(
    "obj",
    [
        ({"target": "score", "numerical_vars": []},),
        ({"target": "score", "numerical_vars": [], "categorical_vars": None},),
        ({"target": "score", "numerical_vars": [], "categorical_vars": []},),
        ({"target": "score", "numerical_vars": None, "categorical_vars": []},),
    ],
)
def test_base_eqn_validation_error(obj):
    """Test the base representation of equations."""
    with pytest.raises(ValidationError):
        BaseEquation.model_validate(obj)
