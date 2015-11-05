#! /usr/bin/env python
# -*- coding: utf-8 -*-

import status as status
from flask import Flask, request, make_response
from flask.ext.api import status
from service import Service
from svc_config import SvcConfig
from svc_utils import SvcUtils
from svc_error import SvcException

app = Flask(__name__)
logger = SvcUtils.get_logger(__name__)


@app.route('/{0:.1f}/admin/status'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def ping():
    try:
        svc = Service()
        svc_response = svc.ping()
        ping_response = SvcUtils.serialize_object(svc_response)
        svc_response = make_response(ping_response)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_200_OK
        return svc_response
    # handle business exceptions
    except (SvcException, ValueError, TypeError) as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_400_BAD_REQUEST
        return svc_response
    # handle server exceptions
    except Exception as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return svc_response


@app.route('/{0:.1f}/chat'.format(SvcConfig.api_version), methods=['POST', 'OPTIONS'])
def save_message():
    try:
        svc = Service()
        svc_response = svc.save_message(request.data)
        svc_response_json = SvcUtils.serialize_object(svc_response)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_201_CREATED
        return svc_response
    # handle business exceptions
    except (SvcException, ValueError, TypeError) as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_400_BAD_REQUEST
        return svc_response
    # handle server exceptions
    except Exception as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return svc_response


@app.route('/{0:.1f}/chat/<int:id>'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def save_message(id):
    try:
        svc = Service()
        svc_response = svc.get_message_by_id(id)
        svc_response_json = SvcUtils.serialize_object(svc_response)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_201_CREATED
        return svc_response
    # handle business exceptions
    except (SvcException, ValueError, TypeError) as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_400_BAD_REQUEST
        return svc_response
    # handle server exceptions
    except Exception as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return svc_response


@app.route('/{0:.1f}/chat/<username>'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def save_message(username):
    try:
        svc = Service()
        svc_response = svc.get_message_by_username(username)
        svc_response_json = SvcUtils.serialize_object(svc_response)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_201_CREATED
        return svc_response
    # handle business exceptions
    except (SvcException, ValueError, TypeError) as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_400_BAD_REQUEST
        return svc_response
    # handle server exceptions
    except Exception as ex:
        svc_response_json = SvcUtils.serialize_object(ex.message)
        svc_response = make_response(svc_response_json)
        svc_response.mimetype = 'application/json'
        svc_response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return svc_response
