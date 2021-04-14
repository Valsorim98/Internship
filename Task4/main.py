#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM4", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

def main():
    """Main function.
    """    
    global client

    # Make a connection
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")

    # Read 4 coils from starting address 16
    response = client.read_coils(
        address=16,
        count=4,
        unit=1)

    print(response.bits[:4])
    if response.bits[:4] == [True]*4:
        print("All relays are on.")
    elif response.bits[:4] == [False]*4:
        print("All relays are off.")
    else:
        print("Error")

    # Turn all coils ON/OFF
    response = client.write_coils(16, [True]*4, unit=1)

    # Read 4 coils from starting address 16
    response = client.read_coils(
        address=16,
        count=4,
        unit=1)

    print(response.bits[:4])
    if response.bits[:4] == [True]*4:
        print("All relays are turned on.")
    elif response.bits[:4] == [False]*4:
        print("All relays are turned off.")
    else:
        print("Error")


    # Read coils
    response = client.read_coils(16, count=4, unit=1)
    print(response.bits[:4])

    # Turn one coil ON/OFF
    #response = client.write_coil(16+2, True, unit=1)

    # Read coils
    response = client.read_coils(16, count=4, unit=1)
    print(response.bits[:4])


if __name__ == "__main__":
    main()
