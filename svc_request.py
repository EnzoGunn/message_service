#! /usr/bin/env python

from svc_config import SvcConfig
from svc_error import SvcException
from svc_utils import SvcUtils


class MessageRequest(object):
    def __init__(self, username, text, timeout=None):
        # recipient of the message
        self.username = username
        # message content
        self.text = text
        # length of time, in seconds, the message should live (set to default if not supplied by client)
        self.timeout = SvcConfig.default_message_timeout if timeout is None else timeout

    def validate_request(self):
        if self.username is None:
            raise SvcException('invalid event request, username is missing')
        if self.text is None:
            raise SvcException('invalid event request, message text is missing')
        if self.timeout is None:
            raise SvcException('invalid event request, message timeout is missing')
        if not SvcUtils.validate_username(self.username):
            error_msg = SvcUtils.error_message('invalid message request, recipient username is not valid', {'username': self.username})
            raise ValueError(error_msg)
        if len(self.text) > SvcConfig.message_length:
            error_msg = SvcUtils.error_message('invalid message request, message length is greater than maximum ({0})'.format(SvcConfig.message_length), {'text': self.text})
            raise ValueError(error_msg)
        if not type(self.timeout) == int:
            error_msg = SvcUtils.error_message('invalid message request, message timeout is not valid', {'timeout': self.timeout})
            raise ValueError(error_msg)
        if self.timeout > SvcConfig.max_message_timeout or self.timeout < 1:
            error_msg = SvcUtils.error_message('invalid message request, message timeout must be between 1 and  ({0})'.format(SvcConfig.max_message_timeout), {'timeout': self.timeout})
            raise ValueError(error_msg)
