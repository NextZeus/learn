#!/usr/bin/env python
# encoding: utf-8

import requests

uri = "http://events.upliveapp.com/ranking/host/receive"

r = requests.post(uri)

print("status_code:")
print(r.status_code)
print(r)
