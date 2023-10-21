"""Classical regression estimator."""
import pandas as pd
import statsmodels.formula.api as smf
from statsmodels.regression.linear_model import OLS, RegressionResultsWrapper

from ecif.calc.eqn.base import BaseEquation
from ecif.utils.logging import get_logger

logger = get_logger(__name__)


class ClassicalRegressionEstimator:
    """Obtain treatment effect estimates based on classical regression."""

    def __init__(
        self,
        data: pd.DataFrame,
        equation: BaseEquation,
        ci_alpha: float = 0.05,
        verbose: bool = True,
    ):
        """Initialize the regressor."""
        self.equation = equation
        self.ci_alpha = ci_alpha
        self.data = data
        self.model: None | OLS = None
        self.results: None | RegressionResultsWrapper = None
        self.verbose = verbose

    def fit(self) -> pd.DataFrame:
        """Fit the regression model."""
        logger.info(f"Creating LR model for equation {self.equation}")
        self.model = smf.ols(self.equation.to_str(), data=self.data)
        self.results = self.model.fit()
        return self._results_to_df(self.results)

    def _results_to_df(self, results: RegressionResultsWrapper):
        """Convert RegressionResultsWrapper summary to a Pandas Dataframe."""
        pvals, coeffs = results.pvalues, results.params

        conf_lower = results.conf_int(self.ci_alpha)[0]
        conf_higher = results.conf_int(self.ci_alpha)[1]

        results_df = pd.DataFrame(
            {"pvals": pvals, "coeff": coeffs, "conf_lower": conf_lower, "conf_higher": conf_higher}
        )

        # Reordering...
        results_df = results_df[["coeff", "pvals", "conf_lower", "conf_higher"]]
        if self.verbose:
            print("#*********** Result summary ***********#")
            print(results_df)
        return results_df
