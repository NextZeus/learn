import requests
from bs4 import BeautifulSoup
import re
import json
import sys
import time
from mysqlmodel import Model
from mysqlmodel import Mysql

def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


class Website:
    session = requests.session()

    htmlParser = BeautifulSoup

    jsonParser = json

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '54.0.2840.98 Safari/537.36'
    }

    def get(self, url, params=None):
        if params is None:
            params = {}

        return self.session.get(url, params=params, headers=self.headers)

    def get_html(self, url, params=None):
        """
        GET请求, 用于网站返回html时
        """
        r = self.get(url,params)
        return self.htmlParser(r.text, 'html.parser')

    def get_json(self, url, params=None):
        """
        GET请求, 用于网站返回json时
        """
        r = self.get(url, params)
        return self.jsonParser.loads(r.text)

    def post_url_encoded(self, url, params):
        pass

    def post_multi_part(self, url, params):
        """
        POST方式：Content-Type:multipart/form-data
        """
        kwargs = dict()
        for(k, v) in params.items():
            kwargs.setdefault(k, (None, v))

        r = self.session.post(url, files=kwargs, headers=self.headers)
        return self.htmlParser(r.text, "html.parser")



