#! /usr/bin/env python


class Message(object):
    def __init__(self, id, user_id, text, expiration_date_utc, created_date_utc):
        # message ID
        self.id = id
        # recipient of the message
        self.user_id = user_id
        # message content
        self.text = text
        # expiration date-time of message (UTC time)
        self.expiration_date_utc = expiration_date_utc
        # date-time message was created (UTC time)
        self.created_date_utc = created_date_utc


class User(object):
    def __init__(self, id, username, created_date_utc):
        # message ID
        self.id = id
        # recipient of the message
        self.username = username
        # date-time message was created (UTC time)
        self.created_date_utc = created_date_utc
