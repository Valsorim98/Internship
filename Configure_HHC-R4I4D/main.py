#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

def read_coils(unit, baud_value):
    """Function to read the coils.

    Args:
        unit (int): The ID of the device.
    """

    global client

    # Make a connection
    client = ModbusClient(method="rtu", port="COM3",
    timeout=0.5, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])

def change_device_id(current_id, new_id):
    """Function to change the device id.

    Args:
        current_id (int): Current device id.
        new_id(int): Set new device id.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    # Change device ID.
    # ATTENTION: register address 1 changes the ID, mistake in the documentation(2)!
    response = client.write_register(address=1, value=6, unit=0)
    print(response)

    state = True

    return state

def change_device_bd(current_id, new_baudrate):
    """Function to change the device baudrate.

    Args:
        current_id (int): Current device id.
        new_baudrate(int): Set new device baudrate.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    # Write device baudrate.
    # ATTENTION: register address 2 changes the baudrate, mistake in the documentation(3)!
    response = client.write_register(address=2, value=4, unit=0)
    print(response)

    state = True

    return state

def identify_device_id_bd(begin_id=1, end_id=247):
    """Function to identify the device ID and baudrate.

    Args:
        begin_id (int): The ID to start searching from.
        end_id (int): The last ID to search to.

    Returns:
        list: List containing the current ID and baudrate of the device.
    """

    global client

    current_id = -1
    baudrate_list = [1200, 2400, 4800, 9600, 19200]
    current_id_bd = []
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        if time_to_stop == True:
            break
        for baud_value in baudrate_list:
            try:
                read_coils(index, baud_value)
                current_id = index
                current_bd = baud_value
                current_id_bd.append(current_id)
                current_id_bd.append(current_bd)
                time_to_stop = True
                print(current_id_bd)
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd

def main():
    """Main function.
    """

    global client

    time_to_stop = False

    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id_bd = identify_device_id_bd()
        state = change_device_id(current_id_bd[0], new_id=6)
        state = change_device_bd(current_id_bd[0], new_baudrate=4)

        if state == True:
            print("Ready...")
            print("Power cycle the device.")
            time_to_stop = True

if __name__ == "__main__":
    main()
