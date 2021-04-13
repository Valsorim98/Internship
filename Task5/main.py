#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM5", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

def main():
    global client

    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")

    response = client.read_coils(
    address=1,
    count=8,
    unit=1)

    print(response.bits)



if __name__ == "__main__":
    main()
