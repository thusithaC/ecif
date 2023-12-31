"""Test helpers and fixtures."""

import pytest

from ecif.sample_data.cibt_fetcher import CIBTSampleDataFetcher


@pytest.fixture()
def online_classroom_simplified_df():
    """online_classroom dataset."""
    return CIBTSampleDataFetcher().fetch_resource("online_classroom")[["falsexam", "format_ol"]]


@pytest.fixture()
def online_classroom_with_controls_df():
    """online_classroom dataset with ."""
    return CIBTSampleDataFetcher().fetch_resource("online_classroom")[
        [
            "falsexam",
            "format_ol",
            "gender",
            "asian",
            "black",
            "hawaiian",
            "hispanic",
            "white",
            "unknown",
        ]
    ]
