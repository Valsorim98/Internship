#!/usr/bin/env python
# -*- coding: utf8 -*-

import requests

url = "https://httpbin.org/get"
payload = {"key1": "value1", "key2": "value2"}
r = requests.get(url, params=payload)
print(f"That is the url: {r.url}")
print(f"That is the status code: {r.status_code}")

if r.status_code == 200:
    print("Success!")
else:
    print("No connection.")


print(f"That is the url content in bytes: {r.content}")

print(f"That is the url content in a string: {r.text}")

print(f"These are the headers: {r.headers}")

# Convert to a dictionary
print(f"That is the content as a dictionary: {r.json()}")

# If we want to access a specific element in the dictionary:
print(r.json()["headers"]["Host"])
