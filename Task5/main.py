#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM5", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

def main():
    """Main function.
    """    
    global client

    # Create a connection with the device
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")

    # Read all the coils
    response = client.read_coils(
    address=1,
    count=12,
    unit=1)

    print(response.bits[:12])

    # Write all the coils ON/OFF for testing
    # The controller has 12 coils, last four coils are turned to False to remind that the request is in 16 bits.
    response = client.write_coils(1, [True]*12+[False]*4, unit=1)

    # Read all the coils
    response = client.read_coils(
    address=1,
    count=12,
    unit=1)

    print(response.bits[:12])


if __name__ == "__main__":
    main()
