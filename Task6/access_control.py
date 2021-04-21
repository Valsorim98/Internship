#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
import datetime
import pymongo
from pymongo import MongoClient

from tokens_base import Tokens
from card_reader import ACT230

class AddToken():
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

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.__client = MongoClient(url)

        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def update(self):

        self.__card_reader.update()

    def __card_reader_cb(self, card_id):

        # if self.__readDB is None:
        #     return

        exp_date_str = input("Type expiration date in day.month.year hour.minute.seconds: ")
        #print(exp_date_str)

        timestamp = int(time.mktime(datetime.datetime.strptime(exp_date_str,
                                             "%d.%m.%Y %H.%M.%S").timetuple()))

        print(timestamp)

        entry = {"token_id": card_id,
                "exp_date": timestamp}

        print(entry)
        #self.__readDB.insert_data("test_db", "tokens_database", entry)
