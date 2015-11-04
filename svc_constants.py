#! /usr/bin/env python


class SvcConstants(object):
    # configuration keys
    API_VERSION_KEY = 'apiVersion'
    LOG_MESSAGE_FORMAT_KEY = 'logMessageFormat'
    IS_DEBUG_MODE_KEY = 'isDebugMode'
    INCLUDE_JSON_METADATA_KEY = 'includeJsonMetadata'
    HTTP_PORT_NUMBER_KEY = 'httpPortNumber'
    HOST_KEY = 'host'
    # default values
    LOG_MESSAGE_FORMAT = '[%(asctime)s UTC] %(levelname)s: %(message)s'
    IS_DEBUG_MODE = False
    INCLUDE_JSON_METADATA = False
    HTTP_PORT_NUMBER = 5000
    HOST = '127.0.0.1'
