#!/usr/bin/env python3
# -*- coding: utf8 -*-

import argparse
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = None
"""Client instance for modbus master.
"""

def read_temperature(unit):
    """Function to read the temperature.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns temperature.
    """

    response = client.read_input_registers(
        address=1,
        count=1,
        unit=unit)

    temperature = int(response.registers[0]) / 10
    print(f"Temperature: {temperature}")
    return temperature

def read_humidity(unit):
    """Function to read the humidity.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns humidity.
    """

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=unit)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")
    return humidity

def identify_device_id():
    """Function to identify device's id.

    Returns:
        int: Returns current device's id as a number.
    """

    global client

    current_id = -1
    # for loop has range from 1 to 254, because of modbus specification.
    for index in range(1, 254):
        try:
            read_temperature(index)
            read_humidity(index)
            print(f"Device id: {index}")
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

    try:
        # Change device id
        response = client.write_register(0x0101, new_id, unit=current_id)
        print(response)
        state = True

    except Exception as e:
        print(e)

    return state

def change_devide_baudrate(current_id, new_baudrate):
    """Function to change device's baudrate.

    Args:
        current_id (int): Current device's ID.
        new_baudrate (int): The new baudrate of the device.
    """

    global client

    response = client.write_register(0x0102, new_baudrate, unit=current_id)
    print(response)


def main():
    """Main function.
    """
    global client

    # Pass arguments from the terminal, if not takes default.
    parser = argparse.ArgumentParser(description='Pass args from terminal.')
    parser.add_argument('--new_id', default=1, type=int, help='Set new device id.')
    parser.add_argument('--port', default="COM5", type=str, help='Modbus COM port.')
    parser.add_argument('--baudrate', default=9600, type=int, help='Rate in symbols per second.')
    parser.add_argument('--new_baudrate', default=9600, type=int, help='Set new device baudrate.')
    parser.add_argument('--identify', help="Identify device's ID")
    args = parser.parse_args()
    # Pass arguments
    new_id = args.new_id
    port = args.port
    baudrate = args.baudrate
    new_baudrate = args.new_baudrate
    identify = args.identify

    # Create a connection with the controller.
    client = ModbusClient(method="rtu", port=port,
    timeout=0.4, stopbits=1, bytesize=8,
    parity="N", baudrate=baudrate)
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")
        return

    # if identify:
    #     print(identify_device_id())
    # else:
    #     print("No device found.")
    #     return

    time_to_stop = False
    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id = identify_device_id()
        state = change_device_id(current_id, new_id)
        change_devide_baudrate(current_id, new_baudrate)

        if state:
            print("Ready...")
            print("Please do power cycle for the device.")
            answer = input("Do you want a new one?: ")

            if answer == "":
                answer = "yes"

            if answer == "no":
                time_to_stop = True


if __name__ == "__main__":
    main()
