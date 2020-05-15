# -*- coding:utf-8 -*-
__author__ = "leo"

import requests


def send_request(url):
    r = requests.get(url)
    return r.status_code


def visit_baidu():
    return send_request("http://www.baidu.com")
