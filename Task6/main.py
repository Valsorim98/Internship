#!/usr/bin/env python3
# -*- coding: utf8 -*-

from card_reader import ACT230
from tokens_base import Tokens
from add_token import AddToken

def main():
    """Main function for the project.
    """

    # Create card reader one
    card_reader = ACT230("COM3", 1914)

    # Call class Tokens
    tokens = Tokens()


    # Call AddToken class
    ac = AddToken(card_reader, tokens)


    #call update method in a while cycle to check for token input non-stop
    while(1):
        ac.update()


if __name__ == "__main__":
    main()
