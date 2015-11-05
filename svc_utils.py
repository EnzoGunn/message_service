#! /usr/bin/env python

import jsonpickle
import logging
import io
import os
import time
import re
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from svc_config import SvcConfig
from svc_constants import SvcConstants


class SvcUtils(object):

    @staticmethod
    def serialize_object(obj):
        return jsonpickle.encode(obj, unpicklable=SvcConfig.include_json_metadata)

    @staticmethod
    def deserialize_object(obj):
        return jsonpickle.decode(obj)

    @staticmethod
    def get_logger(class_name):
        logging.Formatter.converter = time.gmtime
        log_level = logging.DEBUG if SvcConfig.is_debug_mode else logging.WARNING
        logging.basicConfig(format=SvcConfig.log_message_format, level=log_level, datefmt=SvcConstants.DATETIME_FORMAT)
        logger = logging.getLogger(class_name)

        if not SvcConfig.is_debug_mode:
            if not os.path.exists(SvcConstants.LOG_FILE_FOLDER):
                os.makedirs(SvcConstants.LOG_FILE_FOLDER)
            handler = TimedRotatingFileHandler(filename=SvcConstants.LOG_FILE_PATH, when='midnight', utc=True)
            handler.suffix = '%Y-%m-%d.log'
            handler.mode = 'a'
            handler_formatter = logging.Formatter(fmt=SvcConfig.logMessageFormat, datefmt=SvcConstants.DATETIME_FORMAT)
            handler.setFormatter(handler_formatter)
            logger.addHandler(handler)

        return logger

    @staticmethod
    def error_message(error_msg, args):
        return '{0} - '.format(error_msg) + ', '.join('{0}: {1}'.format(key, str(value)) for key, value in args.items())

    @staticmethod
    def read(*names, **kwargs):
        with io.open(
            os.path.join(os.path.dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
        ) as fp:
            return fp.read()

    @staticmethod
    def get_build_version():
        version_file = SvcUtils.read('__init__.py')
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

    @staticmethod
    def regex_validate(regex, msg):
        return re.match(regex, msg)

    @staticmethod
    def validate_username(username):
        is_valid = True
        if SvcConfig.username_validation_regex is not None:
            is_valid = SvcUtils.regex_validate(SvcConfig.username_validation_regex, username)
        return is_valid
