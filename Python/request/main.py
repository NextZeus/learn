#!/usr/bin/env python
# encoding: utf-8

import json
import requests
from requests import exceptions

URL = 'http://api.github.com'
AUTH = ('imoocdemo','imoocdemo123')
def build_uri(endpoint):
    uri = '/'.join([URL,endpoint])
    print '>>>>URI:'
    print uri
    return uri

def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
    response = requests.get(build_uri('user/emails'),auth=AUTH)
    print better_print(response.txt)

def params_request():
    #get user list
    response = requests.get(build_uri('users'),params={'since':'11'})
    print response.request.headers
    print response.url

def json_request():
    json = {'name':'babymooc2'}
    #update user info
    #response = requests.patch(build_uri('user'),auth=AUTH,json=json)
    response = requests.post(build_uri('user/email'),auth=AUTH,json=['helloworld@org.com'])
    print response.request.headers
    print response.request.body
    print response.status_code

def timeout_request():
    try:
        response = requests.get(build_uri('user/emails'),timeout=0.1)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print '>>>>Timeout:'
        print e.message
    except exceptions.HTTPError as e:
        print '>>>>HTTPError:'
        print e.message
    else :
        print response

if __name__ == '__main__':
    params_request()
