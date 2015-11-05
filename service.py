#! /usr/bin/env python

from svc_config import SvcConfig
from svc_utils import SvcUtils
from svc_response import PingDto
from svc_error import SvcException
from svc_request import MessageRequest

logger = SvcUtils.get_logger(__name__)


class Service(object):
    def ping(self):
        ping = PingDto(SvcConfig.api_version, SvcUtils.get_build_version(), SvcConfig.is_debug_mode)
        return ping

    def save_message(self, request):
        if request is None or request == '':
            error = 'No request body submitted'
            logger.critical(error)
            raise SvcException(error)
        request_dict = SvcUtils.deserialize_object(request)
        message_request = type('MessageRequest', (object,), request_dict)
        connection_string = SvcConfig.dbConnectionStr
        #data_access = DataAccess(connection_string)
        #registration_svc = DeviceRegistrationSvc(data_access=data_access, float_errors=True)
        #registration_svc.process_request(device_list=device_list, installation_guid=installation_guid)
        # return message.id

    def get_message_by_username(self, username):
        # test

    def get_message_by_id(self, id):
        # test