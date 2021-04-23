#!/usr/bin/env python3
# -*- coding: utf8 -*-

import configparser
import os

class CreateConfig():
    """Class CreateConfig.
    """

    def create_config(self):
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
        os.chdir("C:/Users/Miro/Documents/Git_repos/Work/Task5/card_reader_mongodb")

        cfgfile = open("config.ini",'w')
        write_config.write(cfgfile)
        cfgfile.close()

        return cfgfile

    def read_config(self):
        """Method to read the config.ini file.
        """        
        read_config = configparser.ConfigParser()
        read_config.read("config.ini")
        section1 = read_config.get("Connection to database", "URL")
        print(f"URL: {section1}")

        return read_config
