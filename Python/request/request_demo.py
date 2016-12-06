#!/usr/bin/env python
# encoding: utf-8
import requests

URL_IP = 'http://127.0.0.1:8000/ip'
URL_GET = 'http://127.0.0.1:8000/get'

def use_simple_request():
    response = requests.get(URL_IP)
    print '>>>> Response Headers:'
    print response.headers
    print '>>>>Response Body:'
    print response.text

def use_params_request():
    params = {'param1':'hello','param2':'world'}
    print 'Request params:'
    print params
    response = requests.get(URL_GET,params=params)
    print '>>>> Response Headers:'
    print response.headers
    print '>>>> Response code:'
    print response.status_code
    print '>>>> Response Body:'
    print response.json()


if __name__ == '__main__':
    print '>>>>use simple request'
    use_simple_request()
    print
    print '>>>>use params request'
    use_params_request()
