#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests

url = "https://httpbin.org/delete"
payload = {"FirstName": "John", "LastName": "Smith"}
r = requests.delete(url, data=payload)
print(r.status_code)
print(r.text)
