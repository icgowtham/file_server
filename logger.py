# -*- coding: utf-8 -*-
"""Logger module."""
import logging

__all__ = 'get_logger'


def get_logger():
    """
    Function to return the logger object handle.

    :param: None
    :return: object
        The logger handle object.
    """
    log_handler = logging.getLogger('file_server')
    if not log_handler.handlers:
        log_handler.setLevel(logging.DEBUG)
        # Adding stream handler to print log messages to the screen
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(
            '[%(asctime)s] [%(levelname)s] [%(filename)s:%(funcName)s::%(lineno)d] %(message)s')
        stream_handler.setFormatter(stream_formatter)
        log_handler.addHandler(stream_handler)
        log_handler.propagate = False
    return log_handler
