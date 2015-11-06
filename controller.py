#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.api import status
from service import Service
from svc_config import SvcConfig
from svc_error import SvcError
from svc_utils import SvcUtils

app = Flask(__name__)
logger = SvcUtils.get_logger(__name__)


@app.route('/v{0:.1f}/admin/status'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def ping():
    try:
        svc = Service()
        svc_response = svc.ping()
        return SvcUtils.handle_response(svc_response, status.HTTP_200_OK)
    except Exception as ex:
        return SvcError.handle_error(ex)


@app.route('/v{0:.1f}/chat'.format(SvcConfig.api_version), methods=['POST', 'OPTIONS'])
def save_message():
    try:
        svc = Service()
        svc_response = svc.save_message(request.data)
        return SvcUtils.handle_response(svc_response, status.HTTP_201_CREATED)
    except Exception as ex:
        return SvcError.handle_error(ex)


@app.route('/v{0:.1f}/chat/<int:message_id>'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def get_message_by_id(message_id):
    try:
        svc = Service()
        svc_response = svc.get_message_by_id(message_id)
        return SvcUtils.handle_response(svc_response, status.HTTP_200_OK)
    except Exception as ex:
        return SvcError.handle_error(ex)


@app.route('/v{0:.1f}/chat/<username>'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def get_message_by_username(username):
    try:
        svc = Service()
        svc_response = svc.get_message_by_username(username)
        return SvcUtils.handle_response(svc_response, status.HTTP_200_OK)
    except Exception as ex:
        return SvcError.handle_error(ex)
