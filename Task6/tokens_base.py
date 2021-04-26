#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
from pymongo import MongoClient

class Tokens():
    """Tokens class.
    """    

    def get_tokens(self):
        """Method to return a database collection.

        Returns:
            object: Database collection.
        """        

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db["whitelist"]

        return collection

    def insert_data(self, db_name, collection_name, card_id, data):
        """Method to update a collection with new documents.

        Args:
            db_name (string): Name of the database.
            collection_name (string): Name of the collection.
            card_id (string): Token code.
            data (dict): Data to be updated to the collection.
        """        

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]

        result = db.whitelist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
