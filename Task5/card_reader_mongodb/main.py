#!/usr/bin/env python3
# -*- coding: utf8 -*-

from date_time import DateTime
from card_reader import ACT230
from tokens_base import Tokens
from io_controller import IOController
from access_control import AccessControl
from create_read_config import CreateConfig


def main():
    """Main function for the project.
    """

    # Create config.ini file
    cc = CreateConfig()
    create_config = cc.create_config()

    # Read config.ini file
    #read_config = cc.read_config()

    # Call class DateTime and date_time method
    date_time = DateTime()
    execution_time = date_time.time_of_execution()

    # Create card reader one
    card_reader = ACT230("COM3", 1914)

    # Call class Tokens and get_tokens method
    tokens = Tokens()

    # Create controller
    controller = IOController("COM5", 1)

    # Call AccessControl class
    ac = AccessControl(card_reader, tokens, controller)

    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()


if __name__ == "__main__":
    main()
