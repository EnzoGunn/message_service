#! /usr/bin/env python
# -*- coding: utf-8 -*-

import status as status
import jsonpickle
from flask import Flask, request, make_response
from flask.ext.api import status
from service import Service
from svc_config import SvcConfig
from svc_utils import SvcUtils

app = Flask(__name__)


@app.route('/{0:.1f}/admin/status'.format(SvcConfig.api_version), methods=['GET', 'OPTIONS'])
def ping():
    svc = Service()
    ping = svc.ping()
    ping_response = SvcUtils.serialize_object(ping)

    svc_response = make_response(ping_response)
    svc_response.mimetype = 'application/json'
    svc_response.status_code = status.HTTP_200_OK
    return svc_response


