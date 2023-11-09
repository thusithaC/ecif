"""This is the main control module."""
from pathlib import Path

from ecif.configs.base_trial_config import BaseTrialConfig
from ecif.utils.logging import get_logger

logger = get_logger(__name__)


class Orchestrator:
    """Main control module in ECIF.

    Orchestrator is responsible for:
     - Loading the Configuration
     - Obtaining data from the data-sources and caching it.
     - Saving experiment data and results objects

    """

    def __init__(
        self,
        config_file: str | Path,
    ):
        """Initialize the orchestrator.

        Args:
            config_file: Path of the configuration file.
        """
        self.config = BaseTrialConfig.from_yaml(config_file)

        # TODO dynamic loading of data
