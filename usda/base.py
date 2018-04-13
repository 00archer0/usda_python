#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json

uri_base = 'http://api.data.gov/'


def get_response_data(uri):
    response = urllib2.urlopen(uri)
    if response.code != 200:
        raise Exception("Error\r\n\tCode: {0}\r\n\tMessage: {1}".format(
            response.code, response.msg))
    data = json.load(response.fp)
    return data


class DataGovClientBase(object):

    def __init__(self, uri_part, api_key, use_format=True):
        self.uri_part = uri_part
        self.key = api_key
        self.use_format = use_format

    def build_uri(self, api, uri_action, **kwargs):
        kwargs['api_key'] = self.key
        if 'format' not in kwargs and self.use_format:
            kwargs['format'] = 'json'
        params = urllib.urlencode(kwargs)
        return "{0}{1}{2}/{3}?{4}".format(
            uri_base, self.uri_part, api, uri_action, params)
