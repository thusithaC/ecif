"""Data fetcher module."""


import pandas as pd

from ecif.utils.logging import get_logger

logger = get_logger(__name__)


class CIBTSampleDataFetcher:
    """Helper class to fetch data from https://github.com/matheusfacure/python-causality-handbook."""

    def __init__(self):
        """Create an instance of CIBTSampleDataFetcher class."""
        self.data_base_path = (
            "https://raw.githubusercontent.com/matheusfacure/"
            "python-causality-handbook/master/causal-inference-for-the-brave-and-true/data"
        )

    def fetch_resource(self, resource_name: str) -> None | pd.DataFrame:
        """Fetch a csv resource from the book repo."""
        try:
            resource_url = f"{self.data_base_path}/{resource_name}.csv"
            logger.info(f"Fetching {resource_url}")
            df_sample = pd.read_csv(resource_url)
        except Exception as err:
            logger.error(f"Error fetching resource {resource_name}", err)
            return None
        return df_sample
