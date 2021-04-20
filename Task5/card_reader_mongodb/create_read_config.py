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
        write_config.add_section("Connection to database")
        write_config.set("Connection to database","URL","mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        write_config.add_section("Card reader")
        write_config.set("Card reader","Port","COM3")
        write_config.add_section("Controller")
        write_config.set("Controller","ID","1")

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
