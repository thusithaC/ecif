"""Dynamic loading of classes."""

import importlib

from ecif.exceptions.core_exceptions import ClassNotFoundException
from ecif.utils.logging import get_logger

logger = get_logger(__name__)


def str_to_class(full_class_name):
    """Return a class instance from a string reference.

    Args:
        full_class_name: Fully qualified class name with module. e.g. module.submodule.MyClass

    Returns: the class (un-initialized)

    """
    parts = full_class_name.split(".")
    class_name = parts[-1]
    if len(parts) > 1:
        module_name = ".".join(parts[0:-1])
    else:
        raise ClassNotFoundException from ValueError("Module name must be present.")
    try:
        module_ = importlib.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)
        except AttributeError as err:
            logger.error("Class does not exist")
            raise ClassNotFoundException from err
    except ImportError as err:
        logger.error("Module does not exist")
        raise ClassNotFoundException from err
    return class_
