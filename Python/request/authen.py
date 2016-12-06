#!/usr/bin/env python
# encoding: utf-8

import requests

AUTH = ('imoocdemo','imoocdemo123')
BASE_URL = "https://api.github.com"

def construct_url(end_point):
    return '/'.join([BASE_URL,end_point])

def basic_auth():
    """
    基本认证
    """

    response = requests.get(construct_url('user'),auth=AUTH)
    print response.json()

def basic_oauth():
    headers = {"Authorization":"token  dd6322fa6c57a548268453dc245cbcdc352a7811"};
    response = requests.get(construct_url('user/emails'),headers=headers)
    print response.request.headers
    print response.status_code


#使用requests的auth模块
from requests.auth import AuthBase

class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token = token

    def __call__(self,r):
        r.headers['Authorization'] = ' '.join(['token',self.token])
        return r

def oauth_advanced():
    auth = GithubAuth('dd6322fa6c57a548268453dc245cbcdc352a7811')
    response = requests.get(construct_url('user/emails'),auth=auth)









