#! /usr/bin/env python


class PingDto(object):
    def __init__(self, api_version, build_version, is_debug_mode):
        self.api_version = api_version
        self.build_version = build_version
        self.is_debug_mode = is_debug_mode


class MessageDto(object):
    def __init__(self, id, text):
        # message ID
        self.id = id
        # message content
        self.text = text


class MessageDetailDto(object):
    def __init__(self, username, text, expiration_date):
        # recipient of the message
        self.username = username
        # message content
        self.text = text
        # expiration date-time of message (UTC time)
        self.expiration_date = expiration_date
