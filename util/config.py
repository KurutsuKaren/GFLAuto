import configparser
import sys
from copy import deepcopy
from util.logger import Logger


class Config(object):
    """Config module that reads and validates the config to be passed to
    azurlane-auto
    """

    def __init__(self, config_file):
        """Initializes the config file by changing the working directory to the
        root azurlane-auto folder and reading the passed in config file.

        Args:
            config_file (string): Name of config file.
        """
        Logger.log_msg("Initializing config module")
        self.config_file = config_file
        self.network = {}
        self.feature = ''
        self.iterations = 0
        self.read()

    def read(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        self.network['service'] = config.get('Network', 'Service')
        self.feature = config.get('To-do', 'Feature')
        self.iterations = config.getint('To-do', 'Times')

        Logger.log_msg("Starting GFLAuto!")
