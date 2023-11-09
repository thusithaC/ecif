"""Test helpers and fixtures."""

from pathlib import Path

import pytest

from ecif.sample_data.cibt_fetcher import CIBTSampleDataFetcher


@pytest.fixture()
def online_classroom_simplified_df():
    """online_classroom dataset."""
    return CIBTSampleDataFetcher().fetch_resource("online_classroom")[["falsexam", "format_ol"]]


@pytest.fixture()
def online_classroom_with_controls_df():
    """online_classroom dataset with control variables."""
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


@pytest.fixture()
def test_configs():
    """Configs used for testing."""
    config_root = Path(__file__).parent / "test_data/test_configs"
    configs = {"cr-online-classroom": config_root / "test_config_cr_online_classroom.yaml"}
    return {k: v.as_posix() for k, v in configs.items()}
