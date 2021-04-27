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
        # Find all the documents in the collections to make them iterable
        whitelist = db.whitelist
        whitelist = whitelist.find()
        blacklist = db.blacklist
        blacklist = blacklist.find()

        # Update the token id from the database
        # doc = db.blacklist.find_one({"_id": "6E536046010080FF"})
        # doc["_id"] = "751E9168661790FF"
        # db.blacklist.insert(doc)
        # db.blacklist.remove({"_id": "6E536046010080FF"})

        # Iterate through blacklist collection
        for item in blacklist:
            db_card_id = item["_id"]
            if db_card_id == card_id:
                print("The token already exists in the blacklist collection.")
                question = input("Do you want me to delete it from blacklist and transfer it to whitelist?: ")
                if question == "yes":
                    # Delete the document from blacklist
                    db.blacklist.delete_one(item)
                    # Insert the document in whitelist
                    db.whitelist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
                if question == "no":
                    break

        # Iterate through whitelist collection
        for item in whitelist:
            db_card_id = item["_id"]
            if db_card_id == card_id:
                print("The token already exists in the whitelist collection.")
                question = input("Do you want me to delete it from whitelist and transfer it to blacklist?: ")
                if question == "yes":
                    # Delete the document from whitelist
                    db.whitelist.delete_one(item)
                    # Insert the document in blacklist
                    db.blacklist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
                if question == "no":
                    break
