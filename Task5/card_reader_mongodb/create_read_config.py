#!/usr/bin/env python3
# -*- coding: utf8 -*-

import configparser
import os

class CreateConfig():
    """Class CreateConfig.
    """

    def read_config(self):
        """Method to create a config.ini file.
        """

        write_config = configparser.ConfigParser()
        write_config.add_section("Database")
        write_config.set("Database","URL","mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        write_config.add_section("Card_Reader")
        write_config.set("Card_Reader","Port","COM3")
        write_config.set("Card_Reader","ID","1")
        write_config.set("Card_Reader","Baudrate","9600")
        write_config.set("Card_Reader","Bytesize","8")
        write_config.set("Card_Reader","Timeout","2")
        write_config.set("Card_Reader","Stopbits","1")
        write_config.add_section("Controller")
        write_config.set("Controller","Port","COM5")
        write_config.set("Controller","ID","1")
        write_config.set("Controller","Method","RTU")
        write_config.set("Controller","Baudrate","9600")
        write_config.set("Controller","Bytesize","8")
        write_config.set("Controller","Parity","None")
        write_config.set("Controller","Timeout","1")
        write_config.set("Controller","Stopbits","1")

        # Change directory
        config_path = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            "config.ini")
        #print(config_path)

        # Create the file if it doesnt exist
        if os.path.isfile(config_path):
            print("config file already exists.")
        if os.path.isfile(config_path) is False:
            print("config file doesnt exist, creating now.")
            cfgfile = open(config_path, "w")
            write_config.write(cfgfile)
            cfgfile.close()
        # Read the file
        read_config = configparser.ConfigParser()
        read_config.read(config_path)

        return read_config
