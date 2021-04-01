#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests

url = "https://httpbin.org/post"
payload = {"FirstName": "John", "LastName": "Smith"}
r = requests.post(url, data=payload)
print(r.url)
print(r.status_code)
print(r.content)
print(r.text)
print(r.headers)
