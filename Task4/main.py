#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults


client = ModbusClient(method="rtu", port="COM4", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

def main():
    global client

    connection = client.connect()
    print(connection)

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

    # turn all coils ON
    response = client.write_coils(16, [True]*4, unit=1)

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

if __name__ == "__main__":
    main()
