#!/usr/bin/env python3
# -*- coding: utf8 -*-

import configparser
import os

class CreateConfig():
    """Class CreateConfig.
    """

    __config_path = None
    """The path to the config file.
    """
    __config = None
    """The config file.
    """

    def __init__(self):
        """Constructor.
        """

        # Change directory
        self.__config_path = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            "config.ini")
        #print(config_path)

        self.__config = configparser.ConfigParser()

    def __create_default_config(self):
        """Create default configuration file.
        """

        if self.__config is None:
            return

        self.__config.add_section("Database")
        self.__config.set("Database","URL","mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.__config.add_section("Card_Reader")
        self.__config.set("Card_Reader","Port","COM3")
        self.__config.set("Card_Reader","ID","1")
        self.__config.set("Card_Reader","Baudrate","9600")
        self.__config.set("Card_Reader","Bytesize","8")
        self.__config.set("Card_Reader","Timeout","2")
        self.__config.set("Card_Reader","Stopbits","1")
        self.__config.add_section("Controller")
        self.__config.set("Controller","Port","COM5")
        self.__config.set("Controller","ID","1")
        self.__config.set("Controller","Method","RTU")
        self.__config.set("Controller","Baudrate","9600")
        self.__config.set("Controller","Bytesize","8")
        self.__config.set("Controller","Parity","None")
        self.__config.set("Controller","Timeout","1")
        self.__config.set("Controller","Stopbits","1")

    def __load_configuration(self):
        """Load configuration file.
        """

        # Load from config file
        self.__config.read(self.__config_path)

    def __save_config(self):
        """Save configuration to file.
        """

        cfg_file = open(self.__config_path, "w")
        self.__config.write(cfg_file)
        cfg_file.close()

    def read(self):
        """Method to create a config.ini file.
        """

        if self.__config is None:
            return

        # Create the file if it doesnt exist.
        if not os.path.isfile(self.__config_path):
            print("Creating new configuration.")
            self.__create_default_config()
            self.__save_config()

        self.__load_configuration()

        return self.__config
