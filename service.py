#! /usr/bin/env python

from data_access import DataAccess
from datetime import datetime, timedelta
from svc_config import SvcConfig
from svc_error import SvcException
from svc_request import MessageRequest
from svc_response import PingDto, MessageId, MessageDto, MessageDetailDto
from svc_utils import SvcUtils


class Service(object):
    def __init__(self):
        connection_string = SvcConfig.db_connection_str
        data_access = DataAccess(connection_string)
        self.data_access = data_access

    def ping(self):
        ping = PingDto(SvcConfig.api_version, SvcUtils.get_build_version(), SvcConfig.is_debug_mode)
        return ping

    def save_message(self, request):
        if request is None or request == '':
            raise SvcException('invalid message request, no valid request was submitted')
        request_dict = SvcUtils.deserialize_object(request)

        try:
            message_request_obj = SvcUtils.get_obj_from_dict(request_dict, 'MessageRequest')
            timeout = message_request_obj.timeout if 'timeout' in request_dict.keys() else None
            message_request = MessageRequest(message_request_obj.username, message_request_obj.text, timeout)
        except:
            raise SvcException(SvcUtils.error_message('invalid message request, request is not valid', {'request': request_dict}))

        # first, validate the request
        message_request.validate_request()
        # create message expiration timestamp
        message_expiration_utc = datetime.utcnow() + timedelta(seconds=message_request.timeout)
        # check if user already exists
        user_id = self.data_access.get_user_id_by_username(message_request.username)

        if user_id == 0:
            user_id = self.data_access.save_user(message_request.username)

        if user_id == 0:
            raise Exception(SvcUtils.error_message('could not create user', {'username': message_request.username}))

        message_id = self.data_access.save_message(user_id, message_request.text, message_expiration_utc)

        if message_id == 0:
            raise Exception(SvcUtils.error_message('could not create message', {'username': message_request.username, 'message': message_request.text}))



        return MessageId(message_id)

    def get_message_by_username(self, username):
        if username is None or username == '':
            raise SvcException('invalid event request, no username was submitted')

        messages = self.data_access.get_messages_by_username(username)

        if len(messages) == 0:
            raise KeyError(SvcUtils.error_message('message(s) not found for user', {'username': username}))

        messages_dto = []

        for message in messages:
            messages_dto.append(MessageDto(message.id, message.text))

        return messages_dto

    def get_message_by_id(self, message_id):
        if message_id < 1:
            raise SvcException('invalid event request, message ID must be greater than 0')

        message = self.data_access.get_message_by_id(message_id)

        if message is None:
            raise KeyError(SvcUtils.error_message('message not found', {'id': message_id}))

        user = self.data_access.get_user_by_id(message.user_id)

        if user is None:
            raise Exception(SvcUtils.error_message('message not found', {'id': message_id}))

        return MessageDetailDto(user.username, message.text, message.expiration_date)
