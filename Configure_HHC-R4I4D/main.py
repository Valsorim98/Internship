#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM5", timeout=0.5, stopbits=1, bytesize=8, parity="N", baudrate=1200)

def read_coils(unit):

    global client

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])

def identify_device_id(begin_id=1, end_id=247):
    """Function to identify device's id.

    Returns:
        int: Returns current device's id as a number.
    """

    global client

    current_id = -1
    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id):
        try:
            read_coils(index)
            current_id = index
            break

        except Exception as e:
            print(f"No device found at id: {index}")

    return current_id

def change_device_id(current_id, new_id):
    """Function to change the device id.

    Args:
        current_id (int): Current device id.
        new_id (int): Set new device id.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    response = client.write_register(address=2, value=1, unit=current_id)
    print(response)
    state = True

    return state

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

    time_to_stop = False

    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id = identify_device_id(1, 247)
        state = change_device_id(current_id, new_id=1)


        if state == True:
            print("Ready...")
            time_to_stop = True

if __name__ == "__main__":
    main()
