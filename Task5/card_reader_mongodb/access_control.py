#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time
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

    __tokens_base = None
    """Tokens database instance.
    """
 
    __controller = None
    """IO Controller
    """

    __unlock_flag = False
    """Unlock flag.
    """

    __time_to_open = 5
    """Time to open the door in [s].
    """

    __unlocked_flag = False

    __last_time = 0

    def __init__(self, card_reader, readDB, controller):
        """Constructor

        Args:
            card_reader (ACT230): Instance of the card reader to work with.
            tokens_base (dict): Tokens database.
        """
    
        self.__card_reader = card_reader

        self.__readDB = readDB
        self.__tokens_base = self.__readDB.get_tokens()

        self.__controller = controller



        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def __card_reader_cb(self, card_id):

        if self.__readDB is None:
            return

        # Time of event
        ts = int(time.time())

        # State of the token for the event.
        token_state = 0

        whitelist = self.__tokens_base["whitelist"]

        wl_flag = False

        url = "mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(url)
        db = client["test_db"]
        collection = db.tokens_database
        collection = collection.find_one({}, {"_id": 0})

        # # Print the codes from whitelist
        # for item in collection["whitelist"]:
        #     print(item["code"])
        
        for item in collection["whitelist"]:

            db_card_id = item["code"]

            if db_card_id == card_id:

                wl_flag = True
                break

        
        blacklist = self.__tokens_base["blacklist"]

        bl_flag = False

        for item in collection["blacklist"]:
            db_card_id = item["code"]
            if db_card_id == card_id:

                bl_flag = True
                break

        if wl_flag and not bl_flag:
            print("Access granted")
            token_state = 1
            self.__unlock_flag = True

        if not wl_flag and bl_flag:
            print("Access denied")
            token_state = 2

        if not wl_flag and not bl_flag:
            print("Unauthorized")
            token_state = 3

        if wl_flag and bl_flag:
            print("System error")
            token_state = 4


        entry = {"timestamp": ts,
            "reader_id": self.__card_reader.reader_id,
            "token_id": card_id,
            "state": token_state,
            "direction": 1}

        self.__readDB.insert_data("test_db", "entries", entry)

    def update(self):

        now_time = time.time()

        if self.__card_reader is not None:
            self.__card_reader.update()

        if self.__unlock_flag and not self.__unlocked_flag:
            self.__controller.set_gpio(0, True)
            self.__last_time = time.time()
            self.__unlocked_flag = True

        if now_time > self.__last_time + self.__time_to_open:
            if self.__unlock_flag and self.__unlocked_flag:
                self.__controller.set_gpio(0, False)
                self.__unlock_flag = False
                self.__unlocked_flag = False

