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
            object: Whitelist collection.
        """        

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        whitelist = db["whitelist"]

        return whitelist

    def insert_data(self, db_name, collection_name, card_id, data):
        """Method to update a collection with new documents.

        Args:
            db_name (string): Name of the database.
            collection_name (string): Name of the collection.
            card_id (string): Token code.
            data (dict): Data to be updated to the collection.
        """        

        # Connection with the client
        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        
        db = client["test_db"]
        whitelist = db.whitelist
        blacklist = db.blacklist

        # Iterate through blacklist collection
        for item in blacklist:
            db_card_id = item["_id"]
            if db_card_id == card_id:
                print("The token already exists in the blacklist collection.")
                question = input("Do you want me to delete it from blacklist and transfer it to whitelist or not?")
                if question == "yes":
                    # Delete the document from blacklist here

                    result = db.whitelist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
                if question == "no":
                    break

        # Iterate through whitelist collection
        for item in whitelist:
            db_card_id = item["_id"]
            if db_card_id == card_id:
                print("The token already exists in the whitelist collection.")
                question = input("Do you want me to delete it from whitelist and transfer it to blacklist or not?")
                if question == "yes":
                    # Delete the document from whitelist here

                    result = db.whitelist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
                if question == "no":
                    break
