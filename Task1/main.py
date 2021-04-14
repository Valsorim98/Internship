#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from card_reader import ACT230
from tokens_base import Tokens
from io_controller import IOController
from access_control import AccessControl


client = ModbusClient(method="rtu", port="COM5", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

def main():
    """Main function for the project.
    """
    global client

    # Create a connection with the controller
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")


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
