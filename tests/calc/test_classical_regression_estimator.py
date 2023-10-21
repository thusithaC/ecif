"""Test the estimator."""

from ecif.calc.creg.creg_estimator import ClassicalRegressionEstimator
from ecif.calc.eqn.base import BaseEquation


def test_classical_regression_estimator_numeric(online_classroom_simplified_df):
    """Test the estimator with numeric variable."""
    equation = BaseEquation.model_validate(
        {"target": "falsexam", "numerical_vars": ["format_ol"], "categorical_vars": None}
    )
    estimator = ClassicalRegressionEstimator(online_classroom_simplified_df, equation)
    results_summary = estimator.fit()
    assert results_summary["pvals"]["format_ol"] < 0.05
    assert isinstance(results_summary["coeff"]["format_ol"], float)
    assert results_summary["conf_lower"]["format_ol"] < results_summary["conf_higher"]["format_ol"]
