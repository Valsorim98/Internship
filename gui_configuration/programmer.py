#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
import configparser
import argparse
from struct import pack, unpack
from tkinter.constants import N, NONE

from pymodbus.client.sync import ModbusSerialClient as ModbusClient

class Programmer():
    """Class programmer.
    """

#region Attributes

    __config = None

    __update_progress = None

#endregion

#region Properties

    @property
    def update_progress(self):

        return self.__update_progress


    @update_progress.setter
    def update_progress(self, value):

        if value is not None:
            self.__update_progress = value

#endregion

#region Constructor

    def __init__(self):
        """Constructor for Programmer class.
        """

        self.__read_config_file()

#endregion

#region Private Methods

    def __read_config_file(self):

        # Change directory
        config_path = os.path.join(
                os.getcwd(),
                os.path.dirname(__file__),
                "config.ini")

        # Read config.ini file.
        self.__config = configparser.ConfigParser()
        self.__config.read(config_path)

#endregion

    def __pa_read_voltage(self, port, baudrate, unit):
        """Method to read the voltage from the power analyzer.

        Args:
            port (str): Port name.
            baudrate (int): Baudrate
            unit (int): Unit ID.

        Returns:
            float: Voltage
        """

        voltage = 0.0

        # Make a connection with the device.
        with ModbusClient(method="rtu", port=port, timeout=0.33, baudrate=baudrate) as client:

            response = client.read_input_registers(address=0, count=2, unit=unit)
            is_err = response.isError()
            if not is_err:

                # Pack the response to bytes from the registers
                response_bytes = pack("<HH", response.registers[1], response.registers[0])

                # Unpack the response as a float
                response_float = unpack("f", response_bytes)

                # Get the actual voltage value.
                voltage = response_float[0]

                # Round the voltage.
                voltage = round(voltage, 2)

        return voltage

    def __pa_identify(self, port, begin_id=1, end_id=247):
        """Method to identify the power analyzer ID and baudrate.

        Args:
            port (str): Name of the serial port.
            begin_id (int): The ID to start searching from.
            end_id (int): The last ID to search to.

        Returns:
            dict: Dict containing the current ID and baudrate of the power analyzer.
        """

        time_to_stop = False
        baudrate_list = [1200, 2400, 4800, 9600]
        current_settings = {}

        # for loop has range from 1 to 247, because of modbus specification.
        for device_id in range(begin_id, end_id):

            # If the device ID and baudrate are found to stop.
            if time_to_stop == True:
                break

            # Search for every baudrate value in the baudrate_list.
            for baudrate in baudrate_list:

                if self.__update_progress is not None:
                    self.__update_progress(25)

                voltage = self.__pa_read_voltage(port, baudrate, device_id)
                if voltage < 100.0:
                    print(f"No device found at ID: {device_id} baudrate: {baudrate}.")
                    continue

                print(f"Device found at ID: {device_id} baudrate: {baudrate}.")
                print(f"Voltage: {round(voltage, 2)}")

                # Append the dictionary with id and baudrate.                    
                current_settings["ID"] = device_id
                current_settings["BAUDRATE"] = baudrate

                # Break the search.
                time_to_stop = True
                break

        return current_settings

    def __pa_change_settings(self, current_settings, new_id, new_baudrate):
        """Method to change the power analyzer ID and baudrate.

        Args:
            current_settings (dict): Current power analyzer settings.
            new_id (int): Set new power analyzer id.
            new_baudrate(int): Set new power analyzer baudrate.

        Returns:
            bool : True if successful, else False.
        """

        # Port
        port = self.__config["POWER_ANALYZER"]["PORT"]

        # Make a connection with the device.
        client = ModbusClient(method="rtu", port=port, timeout=0.33,    baudrate=current_settings["BAUDRATE"])
        client.connect()

        # To store which device is configured.
        device_configured = {}

        state = False

        # CHANGING ID:
        # Pack new_id from float to bytes.
        byte_value = pack("f", new_id)

        # Unpack bytes to binary.
        unpack_value = unpack("<HH", byte_value)

        # Append the lower number on last position for little-endian.
        id_regs_values = []
        id_regs_values.append(unpack_value[1])
        id_regs_values.append(unpack_value[0])

        # Write registers 20,21 with the float number to change the ID.
        # Only values from 1 to 247 can be passed.
        if new_id < 1 or new_id > 247:
            raise argparse.ArgumentTypeError("Invalid value! Insert 1 ~ 247.")
        else:
            response = client.write_registers(20, id_regs_values, unit=current_settings["ID"])
            print(response)
            state = True

        # CHANGING BAUDRATE:
        # Pack new_baudrate from float to bytes.
        baudrate_byte_value = pack("f", new_baudrate)

        # Unpack bytes to binary.
        bd_unpack_values = unpack("<HH", baudrate_byte_value)

        # Append the lower number on last position for little-endian.
        bd_regs_values = []
        bd_regs_values.append(bd_unpack_values[1])
        bd_regs_values.append(bd_unpack_values[0])

        # Write registers 28,29 with the float number to change the baudrate.
        # Only values equal to 2400, 4800, 9600 or 1200 baudrate can be passed.
        if new_baudrate != 0 and new_baudrate != 1 and new_baudrate != 2 and new_baudrate != 5:
            raise argparse.ArgumentTypeError("Invalid value! Insert 0, 1, 2 or 5.")
        else:
            response = client.write_registers(28, bd_regs_values, unit=current_settings["ID"])
            print(response)
            state = True

        if state:
            print("Please do power cycle for the device.")
            device_configured["device"] = "POWER_ANALYZER"
            # Shows a pop up.
            # super().show_pop_up(device_configured)

        return state


    def __sensor_read_params(self, port, baudrate, unit):
        """Method to read the temperature and humidity from a sensor.

        Args:
            port ([type]): [description]
            baudrate ([type]): [description]
            unit (int): Unit id.

        Returns:
            float: Returns temperature.
        """

        # PArameters dictionary.
        params = {}
        params["temperature"] = 0.0
        params["humidity"] = 0.0
        
        try:

            # Make a connection with the device.
            with ModbusClient(method="rtu", port=port, timeout=0.33, baudrate=baudrate) as client:

                # Read temperature:
                response = client.read_input_registers(address=1, count=1, unit=unit)
                is_err = response.isError()
                if not is_err:
                    params["temperature"] = int(response.registers[0]) / 10

                # Read humidity.
                response = client.read_input_registers(address=2, count=1, unit=unit)
                is_err = response.isError()
                if not is_err:
                    params["humidity"] = int(response.registers[0]) / 10
        
        except Exception as e:
            pass
        
        return params

    def __sensor_identify(self, port, begin_id=1, end_id=247):
        """Method to identify the sensor ID and baudrate.

        Args:
            port (str): Port
            begin_id (int, optional): Defaults to 1.
            end_id (int, optional): Defaults to 247.

        Returns:
            dict: Current ID and baudrate of the sensor.
        """

        time_to_stop = False
        baudrate_list = [9600, 14400, 19200]
        current_settings = {}

        # for loop has range from 1 to 247, because of modbus specification.
        for device_id in range(begin_id, end_id):

            # If the device ID and baudrate are found to stop.
            if time_to_stop == True:
                break

            # Search for every baudrate value in the baudrate_list.
            for baudrate in baudrate_list:

                if self.__update_progress is not None:
                    self.__update_progress(25)

                params = self.__sensor_read_params(port, baudrate, device_id)
                if (params["temperature"] <= 0.0 or params["humidity"] <= 0.0):
                    print(f"No device found at ID: {device_id} baudrate: {baudrate}.")
                    continue

                # print device parameters.
                print(f"Device found at ID: {device_id} baudrate: {baudrate}.")
                print("Temp: {}; Hum: {}".format(params["temperature"], params["humidity"]))

                # Append the dictionary with id and baudrate.
                current_settings["ID"] = device_id
                current_settings["BAUDRATE"] = baudrate

                # stop the cycle.
                time_to_stop = True
                break

        return current_settings

    def __sensor_change_settings(self, current_settings, new_id, new_baudrate):
        """Change the sensor ID and baudrate.

        Args:
            current_settings (dict): Current sensor id.
            new_id (int): Set new sensor id.
            new_baudrate (int): New baudrate.

        Raises:
            argparse.ArgumentTypeError: Invalid new ID: [1 ~ 247]
            argparse.ArgumentTypeError: Invalid baudrate: [9600, 14400, 19200]

        Returns:
            bool: Is the change succeeded.
        """

        # Only values from 1 to 247 can be passed.
        if new_id < 1 or new_id > 247:
            raise argparse.ArgumentTypeError("Invalid new ID: [1 ~ 247]")

        # Only values equal to 9600, 14400 or 19200 can be passed.
        if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
            raise argparse.ArgumentTypeError("Invalid baudrate: [9600, 14400, 19200]")

        # Port
        port = self.__config["POWER_ANALYZER"]["PORT"]

        state = 0

        # Make a connection with the device.
        with ModbusClient(method="rtu", port=port, timeout=0.33, baudrate=current_settings["BAUDRATE"]) as client:

            response = client.write_register(0x0101, new_id, unit=current_settings["ID"])
            is_err = response.isError()
            if not is_err:
                print(response)
                state += 1

            response = client.write_register(0x0102, new_baudrate, unit=current_settings["ID"])
            is_err = response.isError()
            if not is_err:
                print(response)
                state += 1

        return state == 2


    def __wi_read_coils(self, unit, baudrate, port):
        """Method to read the coils.

        Args:
            unit (int): The ID of the device.
            baudrate (int): Baudrate value.
            port (str): Port

        Returns:
            list: List of bits.
        """

        # Response result.
        bits = []

        # Make a connection.
        with ModbusClient(method="rtu", port=port, timeout=0.33, baudrate=baudrate) as client:

            response = client.read_coils(address=16, count=4, unit=unit)
            is_err = response.isError()
            if not is_err:
                bits = response.bits

        return bits

    def __wi_identify(self, begin_id, end_id, port):
        """Method to identify the white island ID and baudrate.

        Args:
            begin_id (int): The ID to start searching from.
            end_id (int): The last ID to search to.

        Returns:
            dict: Dict containing the current ID and baudrate of the white island.
        """

        time_to_stop = False
        baudrate_list = [1200, 2400, 4800, 9600, 19200]
        current_settings = {}

        # for loop has range from 1 to 247, because of modbus specification.
        for device_id in range(begin_id, end_id+1):

            # If the device ID and baudrate are found to stop.
            if time_to_stop == True:
                break

            # Search for every baudrate value in the baudrate_list.
            for baudrate in baudrate_list:

                if self.__update_progress is not None:
                    self.__update_progress(25)

                coils_status = self.__wi_read_coils(device_id, baudrate, port)
                if len(coils_status) <= 0:
                    print(f"No device found at ID: {device_id} baudrate: {baudrate}.")
                    continue

                # Append the dictionary with id and baudrate.
                current_settings["ID"] = device_id
                current_settings["BAUDRATE"] = baudrate
                    
                print(f"Device found at ID: {device_id} baudrate: {baudrate}.")
                print("Coils: {}".format(coils_status))

                time_to_stop = True
                break

        return current_settings

    def __wi_change_settings(self, current_settings, new_id, new_baudrate):
        """Method to change the white island id and baudrate.

        Args:
            current_settings (dict): Current device id.
            new_id(int): Set new device id.
            new_baudrate(int): Set new device baudrate.

        Raises:
            argparse.ArgumentTypeError: Invalid ID! Insert [1 ~ 247]
            argparse.ArgumentTypeError: Invalid baudrate! Insert [1, 2, 3, 4, 5]

        Returns:
            bool : True if successful, else False.
        """

        # Only values from 1 to 247 can be passed.
        if new_id < 1 or new_id > 247:
            raise argparse.ArgumentTypeError("Invalid ID! Insert [1 ~ 247]")

        # Only values equal to 9600, 14400 or 19200 can be passed.
        if new_baudrate != 1 and new_baudrate != 2 and new_baudrate != 3 and new_baudrate != 4 and new_baudrate != 5:
            raise argparse.ArgumentTypeError("Invalid baudrate! Insert [1, 2, 3, 4, 5]")

        # Port
        port = self.__config["POWER_ANALYZER"]["PORT"]

        state = 0

        # Make a connection with the device.
        with ModbusClient(method="rtu", port=port, timeout=0.33, baudrate=current_settings["BAUDRATE"]) as client:

            # Change device ID.
            # ATTENTION: register address 1 changes the ID, mistake in the documentation(2)!
            response = client.write_register(address=1, value=6, unit=0)
            is_err = response.isError()
            if not is_err:
                print(response)
                state += 1

            # Write device baudrate.
            # ATTENTION: register address 2 changes the baudrate, mistake in the documentation(3)!
            response = client.write_register(address=2, value=4, unit=0)
            is_err = response.isError()
            if not is_err:
                print(response)
                state += 1

        return state == 2

#endregion

#region Public Methods

    def config_power_analyser(self):

        if self.__config == None:
            return

        # Get ID, baudrate and port values for the power analyzer.
        power_analyzer_port = self.__config["POWER_ANALYZER"]["PORT"]
        power_analyzer_id = int(self.__config["POWER_ANALYZER"]["ID"])
        power_analyzer_bd = int(self.__config["POWER_ANALYZER"]["B9600"])

        # Call identify and change functions.
        current_settings = self.__pa_identify(power_analyzer_port)
        self.__pa_change_settings(current_settings, power_analyzer_id, power_analyzer_bd)

    def config_upper_sensor(self):

        if self.__config == None:
            return

        # Get ID, baudrate and port values for the upper sensor.
        sensor_id = int(self.__config["UPPER_SENSOR"]["ID"])
        sensor_bd = int(self.__config["UPPER_SENSOR"]["BAUDRATE"])
        sensor_port = self.__config["UPPER_SENSOR"]["PORT"]

        # Call identify and change functions.
        current_settings = self.__sensor_identify(sensor_port)
        self.__sensor_change_settings(current_settings, sensor_id, sensor_bd)

    def config_middle_sensor(self):

        if self.__config == None:
            return

        # Get ID, baudrate and port values for the upper sensor.
        sensor_id = int(self.__config["MIDDLE_SENSOR"]["ID"])
        sensor_bd = int(self.__config["MIDDLE_SENSOR"]["BAUDRATE"])
        sensor_port = self.__config["MIDDLE_SENSOR"]["PORT"]

        # Call identify and change functions.
        current_settings = self.__sensor_identify(sensor_port)
        self.__sensor_change_settings(current_settings, sensor_id, sensor_bd)

    def config_lower_sensor(self):

        if self.__config == None:
            return

        # Get ID, baudrate and port values for the upper sensor.
        sensor_id = int(self.__config["LOWER_SENSOR"]["ID"])
        sensor_bd = int(self.__config["LOWER_SENSOR"]["BAUDRATE"])
        sensor_port = self.__config["LOWER_SENSOR"]["PORT"]

        # Call identify and change functions.
        current_settings = self.__sensor_identify(sensor_port)
        self.__sensor_change_settings(current_settings, sensor_id, sensor_bd)

    def config_white_island(self):

        if self.__config == None:
            return

        # Get ID, baudrate and port values for the white island.
        white_island_id = int(self.__config["WHITE_ISLAND"]["ID"])
        white_island_bd = int(self.__config["WHITE_ISLAND"]["B9600"])
        str_white_island_port = self.__config["WHITE_ISLAND"]["PORT"]


        # Call identify and change functions.
        current_settings = self.__wi_identify(1, 247, str_white_island_port)
        self.__wi_change_settings(current_settings, white_island_id, white_island_bd)

#endregion
