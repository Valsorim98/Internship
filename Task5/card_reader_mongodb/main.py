#!/usr/bin/env python3
# -*- coding: utf8 -*-

from card_reader import ACT230
from tokens_base import Tokens
from io_controller import IOController
from access_control import AccessControl


def main():
    """Main function for the project.
    """

    # Create card reader one
    card_reader = ACT230("COM3")

    # Call class Tokens and get_database method
    tokens = Tokens()
    tbase = tokens.get_database()

    # Create controller
    controller = IOController()

    # Call AccessControl class
    ac = AccessControl(card_reader, tbase, controller)


    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()

if __name__ == "__main__":
    main()
