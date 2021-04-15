#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


class IOController():

    __client = None
    """Instance of the controller.
    """

    __coils = [False]*12

    def __init__(self):

        self.__client = ModbusClient(method="rtu", port="COM5", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

        # Create a connection with the controller
        connection = self.__client.connect()

        if connection:
            print("Connected with the controller")
        else:
            print("No connection with controller")
        

    def set_gpio(self, pin, state):
        """Write coil if given token is whitelisted.

        Args:
            pin (int): Relay index
            state (bool): Relay state
        """

        # Pin is index 0 by default
        #self.__coils[pin] = state
        response = self.__client.write_coils(16, [True]*4, unit=1)

        print("set_gpio({}, {})".format(pin, state))

        # Read all the coils
        response = self.__client.read_coils(
        address=16,
        count=4,
        unit=1)

        print(response.bits[:4])
