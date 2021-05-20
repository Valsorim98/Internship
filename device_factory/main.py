#!/usr/bin/env python3
# -*- coding: utf8 -*-

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



def read_temperature(id):
    """Function to read the temperature.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns temperature.
    """

    global client

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

    global client

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=id)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")

    return humidity

def change_sensor_id(id, new_id):
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
        print('Invalid value! Insert 1 ~ 247.')
        return
    else:
        response = client.write_register(0x0101, new_id, unit=id)
        print(response)
        state = True

    return state

def change_sensor_baudrate(id, new_baudrate):
    """Function to change device's baudrate.

    Args:
        current_id (int): Current device's ID.
        new_baudrate (int): The new baudrate of the device.
    """

    global client

    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
        print("Invalid value! Insert 9600, 14400 or 19200.")
        return
    else:
        response = client.write_register(0x0102, new_baudrate, unit=id)
        print(response)
        state = True

    return state


def create_configuration(barcode_data):
    
    device_configuration = []

    # Split the string data.
    bc_data_split = barcode_data.split("/")

    # Get vendor.
    vendor = bc_data_split[0]

    # Get model.
    model = bc_data_split[1]

    # Sleep for two seconds after a barcode is given
    time.sleep(2)

    # Check which barcode is given
    if vendor == "Donkger" and model == "XY-MD02":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 9600 and\
             baudrate_value != 14400 and\
              baudrate_value != 19200:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("sensor")

    elif vendor == "Eastron" and model == "SDM120":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 1200 and\
             baudrate_value != 2400 and\
              baudrate_value != 4800 and\
              baudrate_value != 9600:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("power_analyzer")

    elif vendor == "Mainland" and model == "HHC-R4I4D":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 1200 and\
             baudrate_value != 2400 and\
              baudrate_value != 4800 and\
              baudrate_value != 9600 and\
              baudrate_value != 19200:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("white_island")

    else:
        print("Not suported device.")

    return device_configuration


def decode_barcode():
    
    device_configuration = []

    # Capture video
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Make a window with these dimensions
    cap.set(3, 640) # 3 Width, 640 pixels
    cap.set(4, 480) # 4 Height, 480 pixels

    camera = True
    while camera == True:
        success, frame = cap.read()

        # Decode the barcode
        for barcode in pyzbar.decode(frame):

            barcode_data = barcode.data.decode('utf-8')

            print("Barcode type {}; content {}".format(barcode.type, barcode_data))

            # Hardcode value for the test.
            if barcode_data == "74897":
                barcode_data = "Donkger/XY-MD02/9600/2"

            device_configuration = create_configuration(barcode_data)

            camera = False

        # Shows the window
        cv2.imshow("Video capture", frame)
        cv2.waitKey(1)

    return device_configuration

def config_device():

    global client

    # Get the return from decode_barcode function
    device_configuration = decode_barcode()

    # Which device is read from the barcode
    device = device_configuration[2]

    # For connection with the sensor
    if device == "sensor":

        # Create a connection with the device.
        client = ModbusClient(method="rtu", port="COM3",
        timeout=1, stopbits=1, bytesize=8,
        parity="N", baudrate=device_configuration[1])
        connection = client.connect()

        if connection:
            print("Connected")
        else:
            print("No connection")
            return

        time_to_stop = False
        # While time_to_stop is not False to identify and change device id and baudrate.
        while not time_to_stop:
            read_temperature(device_configuration[0])
            read_humidity(device_configuration[0])

            answer = input("Do you want to change the sensor ID? ")
            if answer == "yes":
                input_id = input("Enter a new ID 1 ~ 247: ")
                new_id = int(input_id)
                state = change_sensor_id(device_configuration[0], new_id)
                print("Sensor ID changed")
            if answer == "no":
                continue
            answer = input("Do you want to change the sensor's baudrate? ")
            if answer == "yes":
                input_bd = input("Enter a new baudrate - 9600, 14400 or 19200: ")
                new_baudrate = int(input_bd)
                state = change_sensor_baudrate(device_configuration[0], new_baudrate)
                print("Sensor baudrate changed.")
            if answer == "no":
                continue

            # If state is True it means that device id changed successfuly.
            if state:
                print("Ready...")
                print("Please do power cycle for the device.")
                time_to_stop = True

            # If the user doesnt want to change the id or baudrate to also stop.
            time_to_stop = True

    # For connection with the power analyzer
    if device == "power_analyzer":
        pass

    # For connetion with the white island
    if device == "white_island":
        pass

def main():
    """Main function.
    """

    config_device()

if __name__ == "__main__":
    main()
