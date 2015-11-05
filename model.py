#! /usr/bin/env python


class Message(object):
    def __init__(self, id, username, text, expiration_date):
        # message ID
        self.id = id
        # recipient of the message
        self.username = username
        # message content
        self.text = text
        # expiration date-time of message (UTC time)
        self.expiration_date = expiration_date
