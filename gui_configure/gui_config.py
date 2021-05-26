#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import filedialog, Text
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import os
import configparser
import argparse

client = None
"""Client instance for modbus master.
"""

def read_temperature(unit, baud_value):
    """Function to read the temperature.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns temperature.
    """

    global client

    client = ModbusClient(method="rtu", port="COM3",
    timeout=0.4, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

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

    global client

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=unit)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")

    return humidity

def change_sensor_id_bd(current_id, new_id, new_baudrate):
    """Function to change the device id and baudrate.

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

    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
        raise argparse.ArgumentTypeError('Invalid value! Insert 9600, 14400 or 19200.')
    else:
        response = client.write_register(0x0102, new_baudrate, unit=current_id)
        print(response)
        state = True

    if state:
        print("Please do power cycle for the device.")

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
    baudrate_list = [9600, 14400, 19200]
    current_id_bd = []
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        if time_to_stop == True:
            break
        for baud_value in baudrate_list:
            try:
                read_temperature(index, baud_value)
                read_humidity(index)
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

    global client

    # Create the window for GUI.
    root = tk.Tk()
    # Set window name.
    root.title("Configuration")
    # Set window size.
    root.geometry("500x500")
    # Set window background.
    root.configure(bg='#A37CF7')

    # Create a frame.
    # frame = tk.Frame(root)
    # frame.pack()

    # Create a connection with the device.
    # client = ModbusClient(method="rtu", port="COM3",
    # timeout=0.4, stopbits=1, bytesize=8,
    # parity="N", baudrate=9600)
    # connection = client.connect()

    # if connection:
    #     print("Connected")
    # else:
    #     print("No connection")
    #     return

    # Change directory
    config_path = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            "config.ini")

    # Read config.ini file.
    config = configparser.ConfigParser()
    configFilePath = config_path
    config.read(configFilePath)

    # Get ID, baudrate and port values for every device.
    str_power_analyzer_id = config['Power_analyzer']['id']
    str_power_analyzer_bd = config['Power_analyzer']['baudrate']
    str_power_analyzer_port = config['Power_analyzer']['port']
    power_analyzer_id = int(str_power_analyzer_id)
    power_analyzer_bd = int(str_power_analyzer_bd)

    str_upper_sensor_id = config['Upper_sensor']['id']
    str_upper_sensor_bd = config['Upper_sensor']['baudrate']
    str_upper_sensor_port = config['Upper_sensor']['port']
    upper_sensor_id = int(str_upper_sensor_id)
    upper_sensor_bd = int(str_upper_sensor_bd)

    str_middle_sensor_id = config['Middle_sensor']['id']
    str_middle_sensor_bd = config['Middle_sensor']['baudrate']
    str_middle_sensor_port = config['Middle_sensor']['port']
    middle_sensor_id = int(str_middle_sensor_id)
    middle_sensor_bd = int(str_middle_sensor_bd)

    str_lower_sensor_id = config['Lower_sensor']['id']
    str_lower_sensor_bd = config['Lower_sensor']['baudrate']
    str_lower_sensor_port = config['Lower_sensor']['port']
    lower_sensor_id = int(str_lower_sensor_id)
    lower_sensor_bd = int(str_lower_sensor_bd)

    str_white_island_id = config['White_island']['id']
    str_white_island_bd = config['White_island']['baudrate']
    str_white_island_port = config['White_island']['port']
    white_island_id = int(str_white_island_id)
    white_island_bd = int(str_white_island_bd)

    label = tk.Label(text="Which device do you want to configure?", fg="white", bg="#A37CF7")
    label.pack()

    # Button to configure the power analyzer.
    power_analyzer = tk.Button(text="Power analyzer", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to configure the upper sensor.
    upper_sensor = tk.Button(text="Upper sensor", width=15, height=2, fg="white", bg="#6DA536",
            command=lambda :[identify_device_id_bd(), change_sensor_id_bd(3, upper_sensor_id, upper_sensor_bd)])
    upper_sensor.pack()

    # Button to configure the middle sensor.
    middle_sensor = tk.Button(text="Middle sensor", width=15, height=2, fg="white", bg="#6DA536",
            command=lambda :[identify_device_id_bd(), change_sensor_id_bd(4, middle_sensor_id, middle_sensor_bd)])
    middle_sensor.pack()

    # Button to configure the lower sensor.
    lower_sensor = tk.Button(text="Lower sensor", width=15, height=2, fg="white", bg="#6DA536",
            command=lambda :[identify_device_id_bd(), change_sensor_id_bd(5, lower_sensor_id, lower_sensor_bd)])
    lower_sensor.pack()

    # Button to configure the white island.
    white_island = tk.Button(text="White island", width=15, height=2, fg="white", bg="#6DA536")
    white_island.pack()

    # Button to read the temperature and humidity.
    temp_humidity = tk.Button(text="Show temperature and humidity", padx=10, pady=5, fg="white",
                            bg="#6DA536", command=lambda :[read_temperature(upper_sensor_id),read_humidity(upper_sensor_id)])
    temp_humidity.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
