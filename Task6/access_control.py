#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pymongo
from pymongo import MongoClient

from tokens_base import Tokens

class AccessControl():
    """Access control
    """

    __card_reader = None
    """Card reader instance.
    """

    __readDB = None
    """Tokens database instance from MongoDB
    """

    def __init__(self, card_reader, readDB):
        """Constructor

        Args:
            card_reader (ACT230): Instance of the card reader to work with.
            tokens_base (dict): Tokens database.
        """
    
        self.__card_reader = card_reader

        self.__readDB = readDB
        self.__tokens_base = self.__readDB.get_tokens()

        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def __card_reader_cb(self, card_id):

        if self.__readDB is None:
            return

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db.tokens_database
        collection = collection.find_one({}, {"_id": 0})

        # # Print the codes from whitelist
        # for item in collection["whitelist"]:
        #     print(item["code"])

        entry = {"token_id": card_id,
                "exp_date": 1672351200}

        self.__readDB.insert_data("test_db", "tokens_database", entry)
