#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import os
import pymongo
from pymongo import MongoClient
import requests


class Tokens():

    def get_database(self):

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

        # Connect to the database
        client = MongoClient(url)
        #print(client)

        # Create database
        db = client["test_db"]

        # Create collection with name tokens_database in the test_db datebase
        collection = db.tokens_database

        # Import database.json file in database
        #result = collection.insert_one(json_content)


        readDB = collection.find_one({}, {"_id": 0})
        #print(readDB)
        
        # Read the values from whitelist, code
        #for elem in readDB["whitelist"]:
            #print(elem["code"])


        return readDB
