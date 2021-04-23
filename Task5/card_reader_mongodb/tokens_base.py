#!/usr/bin/env python
# -*- coding: utf8 -*-

import json
import os
import pymongo
from pymongo import MongoClient

from date_time import DateTime


class Tokens():

    __mydate = DateTime()

    def get_database(self):
        """Read the database

        Returns:
            dict: Collection from the database
        """        
        
        # Read database.json file
        # dir_path = os.path.abspath(os.path.dirname(__file__))
        # file_path = os.path.join(dir_path, "database.json")
        
        # json_content = None
        # with open(file_path, 'r') as f:
        #     content = f.read()
        #     json_content = json.loads(content)

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

    def create_collection(self, db_name, collection_name):
        """Method to create a collection in the database.

        Args:
            db_name (object): Database name
            collection_name (object): Collection name

        Returns:
            object: collection name
        """        

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

        # Connect to the database
        client = MongoClient(url)
        #print(client)

        db = client[db_name]

        # Create the collection in the database if it doesnt exist
        if db.get_collection(collection_name) == None:
            # Create collection in the datebase
            collection = db.create_collection(collection_name)
            return collection
        else:
            return db.get_collection(collection_name)

    def get_tokens(self):

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db["whitelist"]

        return collection

    def insert_data(self, db_name, collection_name, data):
        """Method to insert new documents in the entries collection.

        Args:
            db_name (string): Name of the database.
            collection_name (string): Name of the collection.
            data (dict): The inserted data.
        """

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        
        client = MongoClient(url)

        db = client[db_name]
        collection = db[collection_name]

        db.entries.insert(data)

