"""Logging helper for ECIF."""

import logging


def get_logger(name: str, level: int = logging.INFO):
    """Get a logger instance."""
    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(module)s : %(message)s", level=level
    )
    return logging.getLogger(name)
