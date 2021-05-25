#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import filedialog, Text
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import os

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
    client = ModbusClient(method="rtu", port="COM3",
    timeout=1, stopbits=1, bytesize=8,
    parity="N", baudrate=9600)
    connection = client.connect()

    if connection:
        print("Connected")
    else:
        print("No connection")
        return

    label = tk.Label(text="Which device do you want to configure?", fg="white", bg="#A37CF7")
    label.pack()

    # Button to configure the power analyzer.
    power_analyzer = tk.Button(text="Power analyzer", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to configure the upper sensor.
    power_analyzer = tk.Button(text="Upper sensor", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to configure the middle sensor.
    power_analyzer = tk.Button(text="Middle sensor", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to configure the lower sensor.
    power_analyzer = tk.Button(text="Lower sensor", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to configure the white island.
    power_analyzer = tk.Button(text="White island", width=15, height=2, fg="white", bg="#6DA536")
    power_analyzer.pack()

    # Button to read the temperature and humidity.
    temp_humidity = tk.Button(text="Show temperature and humidity", padx=10, pady=5, fg="white",
                            bg="#6DA536", command=lambda :[read_temperature(2),read_humidity(2)])
    temp_humidity.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
