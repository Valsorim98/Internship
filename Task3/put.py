#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests

url = "https://httpbin.org/put"
payload = {"FirstName": "John", "LastName": "Smith"}
r = requests.put(url, data=payload)
print(r.status_code)
print(r.text)
