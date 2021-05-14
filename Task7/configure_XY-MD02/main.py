#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""
Configure XY-MD02 device.

Copyright (C) [2021] [Miroslav Stanchev]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

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
    baudrate_list = [9600, 14400, 19200]
    current_id_bd = []
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        if time_to_stop == True:
            break
        for baud_value in baudrate_list:
            try:
                read_temperature(index)
                read_humidity(index)
                current_id = index
                current_bd = baud_value
                current_id_bd.append(current_id)
                current_id_bd.append(current_bd)
                time_to_stop = True
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd

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
        response = client.write_register(0x0101, new_id, unit=current_id)
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

    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
        raise argparse.ArgumentTypeError('Invalid value! Insert 9600, 14400 or 19200.')
    else:
        response = client.write_register(0x0102, new_baudrate, unit=current_id)
        print(response)


def main():
    """Main function.
    """

    global client

    # Pass arguments from the terminal, if not takes default.
    parser = argparse.ArgumentParser(description='Pass args from terminal.')
    parser.add_argument('--new_id', default=1, type=int, help='Set new device id.')
    parser.add_argument('--port', default="COM3", type=str, help='Modbus COM port.')
    parser.add_argument('--baudrate', default=9600, type=int, help='Rate in symbols per second.')
    parser.add_argument('--new_baudrate', default=9600, type=int, help='Set new device baudrate.')
    parser.add_argument('--identify', default="False", type=str, help="Identify device's ID.")
    parser.add_argument('--begin_id', default=1, type=int, help="The begin ID of the device to search from.")
    parser.add_argument('--end_id', default=247, type=int, help="The end ID of the device to stop searching.")
    args = parser.parse_args()

    # Pass arguments
    new_id = args.new_id
    port = args.port
    baudrate = args.baudrate
    new_baudrate = args.new_baudrate
    identify = args.identify
    begin_id = args.begin_id
    end_id = args.end_id

    # Create a connection with the device.
    client = ModbusClient(method="rtu", port=port,
    timeout=0.4, stopbits=1, bytesize=8,
    parity="N", baudrate=baudrate)
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")
        return


    if identify == "True":
        current_id_bd = identify_device_id_bd(begin_id, end_id)
        print("Device ID: {}".format(current_id_bd[0]))
        print("Device baudrate: {}".format(current_id_bd[1]))
        return
    if identify == "False":
        pass
    if identify != "True" and identify != "False":
        raise argparse.ArgumentTypeError('Invalid value! Set value to True.')


    time_to_stop = False
    # While time_to_stop is not False to identify and change device id.
    while not time_to_stop:
        current_id_bd = identify_device_id_bd(begin_id, end_id)
        state = change_device_id(current_id_bd[0], new_id)
        change_devide_baudrate(current_id_bd[0], new_baudrate)

        # If state is True it means that device id changed successfuly.
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
