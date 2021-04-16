#!/usr/bin/env python3
# -*- coding: utf8 -*-

from date_time import DateTime
from card_reader import ACT230
from tokens_base import Tokens
from io_controller import IOController
from access_control import AccessControl


def main():
    """Main function for the project.
    """

    # Call class DateTime and date_time method
    date_time = DateTime()
    execution_time = date_time.time_of_execution()

    # Create card reader one
    card_reader = ACT230("COM3", 1914)

    # Call class Tokens and get_database method
    tokens = Tokens()
    tbase = tokens.get_database()
    tokens.create_collection('test_db', 'entries')

    # Create controller
    controller = IOController()

    # Call AccessControl class
    ac = AccessControl(card_reader, tbase, controller)


    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()



if __name__ == "__main__":
    main()
