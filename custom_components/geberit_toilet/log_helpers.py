from __future__ import annotations
import logging

def _geberit_get_disabled_logger(name):
    logger = logging.getLogger(name)
    logger.handlers.clear()
    logger.addHandler(logging.NullHandler())
    logger.setLevel(logging.CRITICAL + 1)
    logger.propagate = False
    logger.disabled = True
    return logger
_LOGGER = _geberit_get_disabled_logger(__name__)
PACKAGE_LOGGER = _geberit_get_disabled_logger('custom_components.geberit_toilet')

def silence_package_logging():
    return

def log_config_summary(*args, **kwargs):
    return

async def ensure_file_logging(*args, **kwargs):
    return

async def configure_logging(*args, **kwargs):
    return

async def async_remove_file_logging(*args, **kwargs):
    return

def device_log_context(method):
    return method

def set_device_log_context(*args, **kwargs):
    return None

def reset_device_log_context(*args, **kwargs):
    return