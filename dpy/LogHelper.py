"""
.. module:: LogHelper
   :synopsis: logging helper

Module: LogHelper

This module defined utils and class related to logging

"""

import datetime
import logging
import os, sys
#import pandas as pd
#import numpy as np

LOGGER = logging.getLogger(__name__)

#region LogConfigurator

class LogConfigurator(object):
    """
    A singleton to handle setup and teardown of logging
    This is clone from phra-py-log
    """

    is_shutdown = False

    def __init__(self, file_path=None):
        formatter = logging.Formatter(
            fmt="%(asctime)-15s %(levelname)s  [%(name)s] %(filename)s:%(lineno)s - %(message)s",
            datefmt='%Y-%m-%d %H:%M:%S')

        root_logger = logging.getLogger()

        # reconfigure console handler to stdout
        self.__remove_console_handlers()
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.name = "console_handler"
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)

        # reconfigure file handler to write to given file
        if file_path:
            self.__remove_file_handlers()
            file_handler = logging.FileHandler(file_path)
            file_handler.name = "file_handler"
            file_handler.setFormatter(formatter)
            root_logger.addHandler(file_handler)

        root_logger.setLevel(logging.INFO)

    @staticmethod
    def __remove_console_handlers():
        root_logger = logging.getLogger()
        current_console_handlers = list(filter(lambda h: h.name == "console_handler", root_logger.handlers))
        for handler in current_console_handlers:
            root_logger.removeHandler(handler)

    @staticmethod
    def __remove_file_handlers():
        root_logger = logging.getLogger()
        current_file_handlers = list(filter(lambda h: h.name == "file_handler", root_logger.handlers))
        for handler in current_file_handlers:
            root_logger.removeHandler(handler)

    @staticmethod
    def init(file_path=None):
        """
        Static method to create/init a configurator
        If a file_path is given, will configurate logging to both console and given file
        """
        return LogConfigurator(file_path)

    @staticmethod
    def shutdown():
        """
        Shutdown existing logging
        """
        logging.shutdown()
        LogConfigurator.is_shutdown = True

#endregion LogConfigurator