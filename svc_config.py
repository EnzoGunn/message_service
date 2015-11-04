#! /usr/bin/env python

import json
import sys
from svc_constants import SvcConstants

# configuration parsing setup
configFilePath = './settings.development.json'

for arg in sys.argv:
    if '.json' in arg:
        configFilePath = arg

with open(configFilePath, 'r') as file:
    settings = json.load(file)


class SvcConfig(object):
    # required parameters
    api_version = settings.get(SvcConstants.API_VERSION_KEY)
    # optional parameters
    host = settings.get(SvcConstants.HOST_KEY, SvcConstants.HOST)
    http_port_number = settings.get(SvcConstants.HTTP_PORT_NUMBER_KEY, SvcConstants.HTTP_PORT_NUMBER)
    include_json_metadata = settings.get(SvcConstants.INCLUDE_JSON_METADATA_KEY, SvcConstants.INCLUDE_JSON_METADATA)
    is_debug_mode = settings.get(SvcConstants.IS_DEBUG_MODE_KEY, SvcConstants.IS_DEBUG_MODE)
    log_message_format = settings.get(SvcConstants.LOG_MESSAGE_FORMAT_KEY, SvcConstants.LOG_MESSAGE_FORMAT)
