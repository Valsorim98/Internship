#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import messagebox
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import os
import configparser
import argparse
from struct import pack, unpack

client = None
"""Client instance for modbus master.
"""

config = None
"""Config instance of the read config file.
"""

def read_sensor_parameters(unit, baud_value, port):
    """Function to read the temperature and humidity from a sensor.

    Args:
        unit (int): Unit id.

    Returns:
        float: Returns temperature.
    """

    global client

    # Make a connection with the device.
    client = ModbusClient(method="rtu", port=port,
    timeout=0.4, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

    # READ TEMPERATURE:
    response = client.read_input_registers(
        address=1,
        count=1,
        unit=unit)

    temperature = int(response.registers[0]) / 10
    print(f"Temperature: {temperature}")

    # READ HUMIDITY:
    response = client.read_input_registers(
        address=2,
        count=1,
        unit=unit)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")

def read_voltage(unit, baud_value, port):
    """Function to read the voltage from the power analyzer.
    """

    global client

    # Make a connection with the device.
    client = ModbusClient(method="rtu", port=port,
    timeout=0.4, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

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

def read_coils(unit, baud_value, port):
    """Function to read the coils.

    Args:
        unit (int): The ID of the device.
    """

    global client

    # Make a connection.
    client = ModbusClient(method="rtu", port=port,
    timeout=0.5, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])

def change_sensor_id_bd(current_id, new_id, new_baudrate):
    """Function to change the sensor id and baudrate.

    Args:
        current_id (int): Current sensor id.
        new_id (int): Set new sensor id.

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
        # Shows a pop up.
        show_pop_up()

    return state

def identify_sensor_id_bd(begin_id, end_id, port):
    """Function to identify the sensor ID and baudrate.

    Args:
        begin_id (int): The ID to start searching from.
        end_id (int): The last ID to search to.

    Returns:
        dict: Dict containing the current ID and baudrate of the sensor.
    """

    global client

    current_id = -1
    baudrate_list = [9600, 14400, 19200]
    current_id_bd = {}
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):

        # If the device ID and baudrate are found to stop.
        if time_to_stop == True:
            break

        # Search for every baudrate value in the baudrate_list.
        for baud_value in baudrate_list:
            try:
                read_sensor_parameters(index, baud_value, port)
                current_id = index
                current_bd = baud_value
                # Append the dictionary with id and baudrate.
                current_id_bd["id"] = current_id
                current_id_bd["baudrate"] = current_bd
                time_to_stop = True
                print(current_id_bd)
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd

def change_power_analyzer_id_bd(current_id, new_id, new_baudrate):
    """Function to change the power analyzer ID and baudrate.

    Args:
        current_id (int): Current power analyzer id.
        new_id (int): Set new power analyzer id.
        new_baudrate(int): Set new power analyzer baudrate.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    # CHANGING ID:
    # Pack new_id from float to bytes.
    byte_value = pack("f", new_id)

    # Unpack bytes to binary.
    unpack_value = unpack("<HH", byte_value)

    # Append the lower number on last position for little-endian.
    regs_value = []
    regs_value.append(unpack_value[1])
    regs_value.append(unpack_value[0])

    # Write registers 20,21 with the float number to change the ID.
    # Only values from 1 to 247 can be passed.
    if new_id < 1 or new_id > 247:
        raise argparse.ArgumentTypeError('Invalid value! Insert 1 ~ 247.')
    else:
        response = client.write_registers(20, regs_value, unit=current_id)
        print(response)
        state = True

    # CHANGING BAUDRATE:
    # Pack new_baudrate from float to bytes.
    baudrate_byte_value = pack("f", new_baudrate)

    # Unpack bytes to binary.
    baudrate_unpack_value = unpack("<HH", baudrate_byte_value)

    # Append the lower number on last position for little-endian.
    baudrate_regs_value = []
    baudrate_regs_value.append(baudrate_unpack_value[1])
    baudrate_regs_value.append(baudrate_unpack_value[0])

    # Write registers 28,29 with the float number to change the baudrate.
    # Only values equal to 2400, 4800, 9600 or 1200 baudrate can be passed.
    if new_baudrate != 0 and new_baudrate != 1 and new_baudrate != 2 and new_baudrate != 5:
        raise argparse.ArgumentTypeError('Invalid value! Insert 0, 1, 2 or 5.')
    else:
        response = client.write_registers(28, baudrate_regs_value, unit=current_id)
        print(response)
        state = True

    if state:
        print("Please do power cycle for the device.")
        # Shows a pop up.
        show_pop_up()

    return state

def identify_power_analyzer_id_bd(begin_id, end_id, port):
    """Function to identify the power analyzer ID and baudrate.

    Args:
        begin_id (int): The ID to start searching from.
        end_id (int): The last ID to search to.

    Returns:
        dict: Dict containing the current ID and baudrate of the power analyzer.
    """

    global client

    current_id = -1
    baudrate_list = [1200, 2400, 4800, 9600]
    current_id_bd = {}
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):

        # If the device ID and baudrate are found to stop.
        if time_to_stop == True:
            break

        # Search for every baudrate value in the baudrate_list.
        for baud_value in baudrate_list:
            try:
                read_voltage(index, baud_value, port)
                current_id = index
                current_bd = baud_value
                # Append the dictionary with id and baudrate.
                current_id_bd["id"] = current_id
                current_id_bd["baudrate"] = current_bd
                time_to_stop = True
                print(current_id_bd)
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd

def change_white_island_id_bd(current_id, new_id, new_baudrate):
    """Function to change the white island id and baudrate.

    Args:
        current_id (int): Current device id.
        new_id(int): Set new device id.
        new_baudrate(int): Set new device baudrate.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    # Change device ID.
    # ATTENTION: register address 1 changes the ID, mistake in the documentation(2)!
    # Only values from 1 to 247 can be passed.
    if new_id < 1 or new_id > 247:
        raise argparse.ArgumentTypeError('Invalid value! Insert 1 ~ 247.')
    else:
        response = client.write_register(address=1, value=6, unit=0)
        print(response)
        state = True

    # Write device baudrate.
    # ATTENTION: register address 2 changes the baudrate, mistake in the documentation(3)!
    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 1 and new_baudrate != 2 and new_baudrate != 3 and new_baudrate != 4 and new_baudrate != 5:
        raise argparse.ArgumentTypeError('Invalid value! Insert 1, 2, 3, 4 or 5.')
    else:
        response = client.write_register(address=2, value=4, unit=0)
        print(response)
        state = True

    if state:
        print("Please do a power cycle for the device.")
        # Show a pop up.
        show_pop_up()

    return state

def identify_white_island_id_bd(begin_id, end_id, port):
    """Function to identify the white island ID and baudrate.

    Args:
        begin_id (int): The ID to start searching from.
        end_id (int): The last ID to search to.

    Returns:
        dict: Dict containing the current ID and baudrate of the white island.
    """

    global client

    current_id = -1
    baudrate_list = [1200, 2400, 4800, 9600, 19200]
    current_id_bd = {}
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):

        # If the device ID and baudrate are found to stop.
        if time_to_stop == True:
            break

        # Search for every baudrate value in the baudrate_list.
        for baud_value in baudrate_list:
            try:
                read_coils(index, baud_value, port)
                current_id = index
                current_bd = baud_value
                # Append the dictionary with id and baudrate.
                current_id_bd["id"] = current_id
                current_id_bd["baudrate"] = current_bd
                time_to_stop = True
                print(current_id_bd)
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd

def show_pop_up():

    # Shows a pop up window when the configuration is done.
    messagebox.showinfo('Done', 'Configuration complete.')

def on_click_power_analyzer():
    """Function to call identify, change and show pop up functions on button click.
    """

    global config

    if config == None:
        return

    # Get ID, baudrate and port values for the power analyzer.
    str_power_analyzer_id = config['Power_analyzer']['id']
    str_power_analyzer_bd = config['Power_analyzer']['for_9600_baudrate']
    str_power_analyzer_port = config['Power_analyzer']['port']
    power_analyzer_id = int(str_power_analyzer_id)
    power_analyzer_bd = int(str_power_analyzer_bd)

    # Call identify and change functions.
    current_settings = identify_power_analyzer_id_bd(1, 247, str_power_analyzer_port)
    change_power_analyzer_id_bd(current_settings["id"], power_analyzer_id, power_analyzer_bd)

def on_click_upper_sensor():
    """Function to call identify, change and show pop up functions on button click.
    """

    global config

    if config == None:
        return

    # Get ID, baudrate and port values for the upper sensor.
    str_upper_sensor_id = config['Upper_sensor']['id']
    str_upper_sensor_bd = config['Upper_sensor']['baudrate']
    str_upper_sensor_port = config['Upper_sensor']['port']
    upper_sensor_id = int(str_upper_sensor_id)
    upper_sensor_bd = int(str_upper_sensor_bd)

    # Call identify and change functions.
    current_settings = identify_sensor_id_bd(1, 247, str_upper_sensor_port)
    change_sensor_id_bd(current_settings["id"], upper_sensor_id, upper_sensor_bd)

def on_click_middle_sensor():
    """Function to call identify, change and show pop up functions on button click.
    """

    global config

    if config == None:
        return

    # Get ID, baudrate and port values for the middle sensor.
    str_middle_sensor_id = config['Middle_sensor']['id']
    str_middle_sensor_bd = config['Middle_sensor']['baudrate']
    str_middle_sensor_port = config['Middle_sensor']['port']
    middle_sensor_id = int(str_middle_sensor_id)
    middle_sensor_bd = int(str_middle_sensor_bd)

    # Call identify and change functions.
    current_settings = identify_sensor_id_bd(1, 247, str_middle_sensor_port)
    change_sensor_id_bd(current_settings["id"], middle_sensor_id, middle_sensor_bd)

def on_click_lower_sensor():
    """Function to call identify, change and show pop up functions on button click.
    """

    global config

    if config == None:
        return

    # Get ID, baudrate and port values for the lower sensor.
    str_lower_sensor_id = config['Lower_sensor']['id']
    str_lower_sensor_bd = config['Lower_sensor']['baudrate']
    str_lower_sensor_port = config['Lower_sensor']['port']
    lower_sensor_id = int(str_lower_sensor_id)
    lower_sensor_bd = int(str_lower_sensor_bd)

    # Call identify and change functions.
    current_settings = identify_sensor_id_bd(1, 247, str_lower_sensor_port)
    change_sensor_id_bd(current_settings["id"], lower_sensor_id, lower_sensor_bd)

def on_click_white_island():
    """Function to call identify, change and show pop up functions on button click.
    """

    global config

    if config == None:
        return

    # Get ID, baudrate and port values for the white island.
    str_white_island_id = config['White_island']['id']
    str_white_island_bd = config['White_island']['for_9600_baudrate']
    str_white_island_port = config['White_island']['port']
    white_island_id = int(str_white_island_id)
    white_island_bd = int(str_white_island_bd)

    # Call identify and change functions.
    current_settings = identify_white_island_id_bd(1, 247, str_white_island_port)
    change_white_island_id_bd(current_settings["id"], white_island_id, white_island_bd)

def create_gui():
    """Function to create GUI form.
    """

    # Create the window for GUI.
    root = tk.Tk()

    # Set window name.
    root.title("Configuration")

    # Prevents resizing.
    root.resizable(False, False)

    # Set window size.
    root_width = 500
    root_height = 500

    # Place the window in the center of the screen.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (root_width/2))
    y_cordinate = int((screen_height/2) - (root_height/2))
    root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

    # Set window background colour.
    root.configure(bg='#A37CF7')

    label = tk.Label(text="Which device do you want to configure?", fg="white", bg="#A37CF7")
    label.config(font=("Courier", 12))
    label.pack(pady=20)

    # Button to configure the power analyzer.
    power_analyzer = tk.Button(
        text="Power analyzer",
        width=15,
        height=2,
        fg="white",
        bg="#6DA536",
        command=on_click_power_analyzer)

    power_analyzer.pack(pady=10)

    # Button to configure the upper sensor.
    upper_sensor = tk.Button(
        text="Upper sensor",
        width=15,
        height=2,
        fg="white",
        bg="#6DA536",
        command=on_click_upper_sensor)

    upper_sensor.pack(pady=10)

    # Button to configure the middle sensor.
    middle_sensor = tk.Button(
        text="Middle sensor",
        width=15,
        height=2,
        fg="white",
        bg="#6DA536",
        command=on_click_middle_sensor)

    middle_sensor.pack(pady=10)

    # Button to configure the lower sensor.
    lower_sensor = tk.Button(
        text="Lower sensor",
        width=15,
        height=2,
        fg="white",
        bg="#6DA536",
        command=on_click_lower_sensor)

    lower_sensor.pack(pady=10)

    # Button to configure the white island.
    white_island = tk.Button(
        text="White island",
        width=15,
        height=2,
        fg="white",
        bg="#6DA536",
        command=on_click_white_island)

    white_island.pack(pady=10)

    root.mainloop()

def read_config():
    """Function to read the config file.
    """

    global config

    # Change directory
    config_path = os.path.join(
            os.getcwd(),
            os.path.dirname(__file__),
            "config.ini")

    # Read config.ini file.
    config = configparser.ConfigParser()
    configFilePath = config_path
    config.read(configFilePath)

def main():
    """Main function for the project.
    """

    read_config()
    create_gui()

if __name__ == "__main__":
    main()
