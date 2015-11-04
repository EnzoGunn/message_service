#! /usr/bin/env python


class PingDto(object):
    def __init__(self, api_version, build_version, is_debug_mode):
        self.api_version = api_version
        self.build_version = build_version
        self.is_debug_mode = is_debug_mode
