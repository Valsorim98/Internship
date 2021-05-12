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
    for index in range(begin_id, end_id):
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

    # Only values from 1 to 247 can be passed.
    if new_id < 1 or new_id > 247:
        raise argparse.ArgumentTypeError('Invalid value! Insert 1 ~ 247.')
    else:
        # Pack new_id from float to bytes
        byte_value = pack("f", new_id)
        # Unpack bytes to binary
        unpack_value = unpack("<HH", byte_value)
        regs_value = []
        # Append the lower number on last position for little-endian
        regs_value.append(unpack_value[1])
        regs_value.append(unpack_value[0])

        # Write registers 20,21 with the float number
        response = client.write_registers(20, regs_value, unit=current_id)
        print(response)

        state = True

    return state

def main():

    global client

    # Create a connection with the device.
    client = ModbusClient(method="rtu", port="COM5",
    timeout=1, parity="N", baudrate=2400)
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")
        return

    # Input from the user for ID - 1 ~ 247.
    input_id = input("Enter a new ID - 1 ~ 247: ")
    new_id = float(input_id)

    time_to_stop = False
    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id = identify_device_id(1, 247)
        state = change_device_id(current_id, new_id)

        # If state is True it means that device id changed successfuly.
        if state is True:
            print("Ready...")
            print("Please do power cycle for the device.")
            time_to_stop = True



if __name__ == "__main__":
    main()
