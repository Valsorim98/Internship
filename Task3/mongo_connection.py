#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
from pymongo import MongoClient
import requests

import json

client = MongoClient()
print(client)

# Create database with name test_db and use it
db = client["test_db"]

url = "https://httpbin.org/get"
payload = {"key1": "value1", "key2": "value2"}
response = requests.get(url, params=payload)

# Create collection with name test_collection in the test_db datebase
test_collection = db.test_collection

content = response.text
json_content = json.loads(content)

print(json_content)


# Save the document in dict type in the database collection
#result = test_collection.insert_one(json_content)

url = "https://www.bloomberg.com/europe"
#payload = {"key1": "value1", "key2": "value2"}
response_2 = requests.get(url)
print(response_2.status_code)

print(response_2.headers)

result = test_collection.insert_one(response_2.headers)
