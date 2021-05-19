#!/usr/bin/env python3
# -*- coding: utf8 -*-

import argparse
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import cv2  # Read image/video input
from pyzbar.pyzbar import decode    # Read barcode
from pyzbar import pyzbar
import numpy as np
import time

client = None
"""Client instance for modbus master.
"""

def decode_barcode():
    """Function to decode barcodes from a live video.

    Returns:
        list: The decoded ID and baudrate of the barcode.
    """

    # Read video
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # 3 Width, 640 pixels
    cap.set(4, 480) # 4 Height, 480 pixels

    # List to store device ID and baudrate
    device_settings = []
    camera = True

    while camera == True:
        success, frame = cap.read()

        # Decode the barcode
        for barcode in pyzbar.decode(frame):
            print("Read a barcode.")
            print(barcode.type)
            print(barcode.data.decode('utf-8'))

            # The barcode data as a string:
            bc_data = "Donkger/XY-MD02/9600/2" # Place barcode.data.decode('utf-8') here
            bc_data_split = bc_data.split("/")[-0:]

            manufacturer = bc_data_split[0]
            model = bc_data_split[1]

            # Sleep for two seconds after a barcode is given
            time.sleep(2)

            # Check if the given barcode is valid
            if model != "XY-MD02" or manufacturer != "Donkger":
                print("Wrong barcode! Insert a valid one.")
                break
            if int(bc_data_split[3]) < 1 or int(bc_data_split[3]) > 247:
                print("Invalid ID number! Insert a valid barcode.")
                break
            if int(bc_data_split[2]) != 9600 and int(bc_data_split[2]) != 14400 and int(bc_data_split[2]) != 19200:
                print("Invalid baudrate! Insert a valid barcode.")
                break

            # If the barcode is valid to store the id and baudrate in a list
            else:
                id = int(bc_data_split[3])
                baudrate = int(bc_data_split[2])

                # If the list is empty to append with id and baudrate
                if not device_settings:
                    device_settings.append(id)
                    device_settings.append(baudrate)
                camera = False      # When closing the window an error pops up

        # Shows the window
        cv2.imshow("Video capture", frame)
        cv2.waitKey(1)

    return device_settings

def read_temperature(id):
    """Function to read the temperature.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns temperature.
    """

    response = client.read_input_registers(
        address=1,
        count=1,
        unit=id)

    temperature = int(response.registers[0]) / 10
    print(f"Temperature: {temperature}")

    return temperature

def read_humidity(id):
    """Function to read the humidity.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns humidity.
    """

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=id)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")

    return humidity

def change_device_id(id, new_id):
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
        response = client.write_register(0x0101, new_id, unit=id)
        print(response)
        state = True

    return state

def change_devide_baudrate(id, new_baudrate):
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
        response = client.write_register(0x0102, new_baudrate, unit=id)
        print(response)


def main():
    """Main function.
    """

    global client

    device_settings = decode_barcode()

    # Pass arguments from the terminal, if not takes default.
    parser = argparse.ArgumentParser(description='Pass args from terminal.')
    parser.add_argument('--id', default=device_settings[0], type=int, help='The device ID to connect to.')
    parser.add_argument('--new_id', default=2, type=int, help='Set new device id.')
    parser.add_argument('--port', default="COM3", type=str, help='Modbus COM port.')
    parser.add_argument('--baudrate', default=device_settings[1], type=int, help='Rate in symbols per second.')
    parser.add_argument('--new_baudrate', default=9600, type=int, help='Set new device baudrate.')
    args = parser.parse_args()

    # Pass arguments
    id = args.id
    new_id = args.new_id
    port = args.port
    baudrate = args.baudrate
    new_baudrate = args.new_baudrate

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

    time_to_stop = False
    # While time_to_stop is not False to identify and change device id and baudrate.
    while not time_to_stop:

        state = change_device_id(device_settings[0], new_id)
        change_devide_baudrate(device_settings[0], new_baudrate)

        # If state is True it means that device id changed successfuly.
        if state:
            print("Ready...")
            print("Please do power cycle for the device.")
            time_to_stop = True

if __name__ == "__main__":
    main()
