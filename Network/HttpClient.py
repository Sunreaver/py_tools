#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import http.client


class HttpClient:
    """docstring for HttpClient"""

    def __init__(self, host):
        super(HttpClient, self).__init__()
        self.http = http.client.HTTPConnection(host)

    def Get(self, url="", body=None, headers={}):
        '''http Get方法'''
        self.http.request("GET", url, body, headers)
        rc = self.http.getresponse()
        if rc.status == http.HTTPStatus.OK:
            return rc.read()
        return ""

    def Post(self, url="", body=None, headers={}):
        '''http Post方法'''
        self.http.request("POST", url, body, headers)
        rc = self.http.getresponse()
        if rc.status == http.HTTPStatus.OK:
            return rc.read()
        return ""

    def ResetHost(self, host):
        '''重新设置Http的host'''
        self.http = http.client.HTTPConnection(host)


class HttpsClient(HttpClient):
    """docstring for HttpsClient"""

    def __init__(self, host):
        super(HttpsClient, self).__init__(host)
        self.http = http.client.HTTPSConnection(host)
