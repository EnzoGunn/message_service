#! /usr/bin/env python

from svc_config import SvcConfig
from svc_utils import SvcUtils


class DummyRequest(object):
    def __init__(self, dummy_attr):
        self.dummy_attr = dummy_attr

    def validate_request(self):
        if self.dummy_attr is None:
            raise Exception('Invalid event request, dummy attribute is missing')
