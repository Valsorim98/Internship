#!/usr/bin/env python3
# -*- coding: utf8 -*-

from card_reader import ACT230
from tokens_base import Tokens
from io_controller import IOController
from access_control import AccessControl
from create_read_config import CreateConfig


def main():
    """Main function for the project.
    """

    # Call CreateConfig class
    cc = CreateConfig()
    # Read config.ini file
    config = cc.read()
    cd_port = config["Card_Reader"]["Port"]
    cd_id = config["Card_Reader"]["ID"]
    io_port = config["Controller"]["Port"]
    io_id = config["Controller"]["ID"]

    # Create card reader one
    card_reader = ACT230(cd_port, cd_id)

    # Call class Tokens and get_tokens method
    tokens = Tokens()

    # Create controller
    controller = IOController(io_port, io_id)

    # Call AccessControl class
    ac = AccessControl(card_reader, tokens, controller)

    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()


if __name__ == "__main__":
    main()
