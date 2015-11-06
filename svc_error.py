#! /usr/bin/env python

from flask import make_response
from flask.ext.api import status
from svc_utils import SvcUtils

logger = SvcUtils.get_logger('message_service')


class SvcException(Exception):
    """Service Exception"""


class Error(object):
    def __init__(self, message):
        self.message = message


class SvcError(object):
    @staticmethod
    def handle_error(exception):
        error_message = exception.message

        if type(exception) == SvcException or type(exception) == ValueError or type(exception) == TypeError:
            status_code = status.HTTP_400_BAD_REQUEST
        elif type(exception) == LookupError and 'has duplicate records' in exception.message:
            status_code = status.HTTP_404_NOT_FOUND
            error_message = exception.message.replace('has duplicate records', 'not found')
        elif type(exception) == KeyError:
            status_code = status.HTTP_404_NOT_FOUND
        elif type(exception) == ReferenceError and exception.message == 'Database connection string is NULL':
            # hide server error from client, and log nature of error
            logger.critical(exception.message)
            error_message = 'internal server error'
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            # hide server error from client, and log nature of error
            logger.critical(exception.message)
            error_message = 'internal server error'
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        error_message_obj = Error(error_message)
        svc_response_json = SvcUtils.serialize_object(error_message_obj)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status_code
        return svc_response
