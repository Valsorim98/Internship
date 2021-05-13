#!/usr/bin/env python3
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from struct import pack, unpack
import argparse

client = None
"""Client instance for modbus master.
"""

def read_voltage(unit):
    """Function to read the voltage.
    """

    response = client.read_input_registers(
    address=0,
    count=2,
    unit=unit)

    # Pack the response to bytes from the registers
    response_bytes = pack("<HH", response.registers[1], response.registers[0])
    # Unpack the response as a float
    response_float = unpack("f", response_bytes)
    voltage = response_float[0]

    print(f"Voltage: {round(voltage, 2)}")
    return round(voltage, 2)

def identify_device_id(begin_id=1, end_id=247):
    """Function to identify device's id.

    Returns:
        int: Returns current device's id as a number.
    """

    global client

    current_id = -1
    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        try:
            read_voltage(index)
            current_id = index
            break

        except Exception as e:
            print(f"No device found at id: {index}")

    print(f"Device ID: {current_id}")
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

    # Pack new_id from float to bytes
    byte_value = pack("f", new_id)

    # Unpack bytes to binary
    unpack_value = unpack("<HH", byte_value)

    # Append the lower number on last position for little-endian
    regs_value = []
    regs_value.append(unpack_value[1])
    regs_value.append(unpack_value[0])

    # Write registers 20,21 with the float number
    response = client.write_registers(20, regs_value, unit=current_id)
    print(response)

    state = True

    return state

def change_devide_baudrate(current_id, new_baudrate):
    """Function to change device's baudrate.

    Args:
        current_id (int): Current device's ID.
        new_baudrate (int): The new baudrate of the device.
    """

    global client

    # Pack new_baudrate from float to bytes
    byte_value = pack("f", new_baudrate)

    # Unpack bytes to binary
    unpack_value = unpack("<HH", byte_value)

    # Append the lower number on last position for little-endian
    regs_value = []
    regs_value.append(unpack_value[1])
    regs_value.append(unpack_value[0])
    response = client.write_registers(28, regs_value, unit=current_id)
    print(response)

def main():

    global client

    # Create a connection with the device.
    client = ModbusClient(method="rtu", port="COM3",
    timeout=1, parity="N", baudrate=9600)
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")
        return

    is_valid_id = False

    while not is_valid_id:
        # Input from the user for ID - 1 ~ 247.
        input_id = input("Enter a new ID - 1 ~ 247: ")

        if input_id.isalpha():
            print("Invalid value! Type a number 1 ~ 247.")

        if input_id.isdigit():
            new_id = float(input_id)

            # Only values from 1 to 247 can be passed.
            if new_id < 1 or new_id > 247:
                print('Invalid value! Insert 1 ~ 247.')

            else:
                is_valid_id = True


    is_valid_baudrate = False

    while not is_valid_baudrate:
        # Input from the user for a new baudrate
        input_baudrate = input("For 2400 baud: 0,\nFor 4800 baud: 1,\nFor 9600 baud: 2,\nFor 1200 baud: 5.\nEnter a new baudrate: ")

        if input_baudrate.isalpha():
            print("Invalid value! Type a number 0, 1, 2 or 5.")

        if input_baudrate.isdigit():
            new_device_baudrate = float(input_baudrate)

            # Only values equal to 2400, 4800, 9600 or 1200 baudrate can be passed.
            if new_device_baudrate != 0 and new_device_baudrate != 1 and new_device_baudrate != 2 and new_device_baudrate != 5:
                print('Invalid value! Insert 0, 1, 2 or 5.')

            else:
                is_valid_baudrate = True


    time_to_stop = False

    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id = identify_device_id()
        state = change_device_id(current_id, new_id)
        new_device_baudrate = change_devide_baudrate(current_id, new_device_baudrate)

        # If state is True it means that device id changed successfuly.
        if state is True:
            print("Ready...")
            print("Please do power cycle for the device.")
            time_to_stop = True

if __name__ == "__main__":
    main()
