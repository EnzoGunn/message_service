#! /usr/bin/env python

from svc_config import SvcConfig
from svc_utils import SvcUtils
from svc_response import PingDto

logger = SvcUtils.get_logger(__name__)


class Service(object):
    def ping(self):
        ping = PingDto(SvcConfig.api_version, SvcUtils.get_build_version(), SvcConfig.is_debug_mode)
        return ping
