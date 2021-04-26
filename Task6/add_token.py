#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
import datetime
import pymongo
from pymongo import MongoClient

from tokens_base import Tokens
from card_reader import ACT230

class AddToken():
    """AddToken class.
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

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.__client = MongoClient(url)
        db = self.__client["test_db"]
        collection = db.whitelist
        collection = collection.find_one({}, {"_id": 0})

        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def update(self):

        self.__card_reader.update()

    def __card_reader_cb(self, card_id):

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db.whitelist
        collection = collection.find_one({}, {"_id": 0})

        # if self.__readDB is None:
        #     return

        #exp_date_str = input("Type GMT expiration date in day.month.year hour.minute.seconds format: ")
        exp_date_str = "30.08.2021 12.12.12"

        # Convert time from string to timestamp format
        timestamp = int(time.mktime(datetime.datetime.strptime(exp_date_str,
                                             "%d.%m.%Y %H.%M.%S").timetuple()))

        print(timestamp)

        data = {"exp_date": timestamp}
        print(card_id)

        for item in collection:
            if card_id == "_id":
                break
            else:
                self.__readDB.insert_data("test_db", "whitelist", card_id, data)
