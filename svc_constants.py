#! /usr/bin/env python

import sys


class SvcConstants(object):
    # configuration keys
    API_VERSION_KEY = 'apiVersion'
    LOG_MESSAGE_FORMAT_KEY = 'logMessageFormat'
    IS_DEBUG_MODE_KEY = 'isDebugMode'
    INCLUDE_JSON_METADATA_KEY = 'includeJsonMetadata'
    HTTP_PORT_NUMBER_KEY = 'httpPortNumber'
    HOST_KEY = 'host'
    DEFAULT_MESSAGE_TIMEOUT_KEY = 'defaultMessageTimeout'
    USERNAME_VALIDATION_REGEX_KEY = 'usernameValidationRegex'
    MESSAGE_LENGTH_KEY = 'messageLength'
    MAX_MESSAGE_TIMEOUT_KEY = 'maxMessageTimeout'
    # default values
    LOG_FILE_FOLDER = './logs'
    LOG_FILE_PATH = './logs/log'
    DATETIME_FORMAT = '%Y-%m-%d %I:%M:%S %p'
    LOG_MESSAGE_FORMAT = '[%(asctime)s UTC] %(levelname)s: %(message)s'
    IS_DEBUG_MODE = False
    INCLUDE_JSON_METADATA = False
    HTTP_PORT_NUMBER = 5000
    HOST = '127.0.0.1'
    DEFAULT_MESSAGE_TIMEOUT = 60
    MESSAGE_LENGTH = 5000
    MAX_MESSAGE_TIMEOUT = sys.maxint
