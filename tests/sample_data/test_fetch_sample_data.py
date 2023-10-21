"""Test fetching sample data."""

import pandas as pd

from ecif.sample_data.cibt_fetcher import CIBTSampleDataFetcher


def test_fetch_sample_data():
    """Test datat fetch as a pandas dataframe."""
    fetcher = CIBTSampleDataFetcher()
    sample_data = fetcher.fetch_resource("app_engagement_push")
    assert isinstance(sample_data, pd.DataFrame)
    assert len(sample_data) > 0
