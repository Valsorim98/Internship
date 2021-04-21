#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
from pymongo import MongoClient

class Tokens():

    def get_tokens(self):

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db["tokens_database"]

        return collection

    def insert_data(self, db_name, collection_name, data):

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db.tokens_database
        collection = collection.find_one({}, {"_id": 0})

        db = client[db_name]
        collection = db[collection_name]

        result = db.tokens_database.update_one(collection["whitelist"], data)
