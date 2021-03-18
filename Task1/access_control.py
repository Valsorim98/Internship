#!/usr/bin/env python3
# -*- coding: utf8 -*-

import time

from tokens_base import Tokens

class AccessControl():
    """Access control
    """

    __card_reader = None
    """Card reader instance.
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

    def __init__(self, card_reader, tokens_base, controller):
        """Constructor

        Args:
            card_reader (ACT230): Instance of the card reader to work with.
            tokens_base (dict): Tokens database.
        """
    
        self.__card_reader = card_reader

        self.__tokens_base = tokens_base

        self.__controller = controller


        if self.__card_reader is not None:
            self.__card_reader.set_card_cb(self.__card_reader_cb)

    def __card_reader_cb(self, card_id):

        if self.__tokens_base is None:
            return


        whitelist = self.__tokens_base["whitelist"]

        wl_flag = False
        
        for item in whitelist:

            db_card_id = item["code"]

            if db_card_id == card_id:

                wl_flag = True
                break

        
        blacklist = self.__tokens_base["blacklist"]

        bl_flag = False
        for item in blacklist:
            db_card_id = item["code"]
            if db_card_id == card_id:

                bl_flag = True
                break

        if wl_flag and not bl_flag:
            print("dobrojelatel")
            self.__unlock_flag = True

        if not wl_flag and bl_flag:
            print("nejelan")

        if not wl_flag and not bl_flag:
            print("nepoznat")

        if wl_flag and bl_flag:
            print("Sistemna greshka")


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

