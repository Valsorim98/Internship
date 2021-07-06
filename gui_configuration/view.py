#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""

Zontromat - Zonal Electronic Automation

Copyright (C) [2020] [POLYGONTeam Ltd.]

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

import threading

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Progressbar

from programmer import Programmer

class View():
    """Class View.
    """

#region Attributes

    __thread_lock = None
    """Thread lock.
    """

    __root = None
    """Root window instance.
    """

    __btn_power_analyser = None
    """Button power analyser config.
    """

    __btn_upper_sensor = None
    """Button upper sensor config.
    """

    __btn_middle_sensor = None
    """Button middle sensor config.
    """

    __btn_lower_sensor = None
    """Button lower sensor config.
    """

    __btn_white_island = None
    """Button white island.
    """

    __progress_bar = None
    """Prograss bar.
    """

    __label = None
    """Label
    """

    __programmer = None
    """Device flasher.
    """

#endregion

#region Constructor

    def __init__(self):
        """Constructor for View class.
        """

        self.__thread_lock = threading.Lock()

        self.__programmer = Programmer()
        self.__programmer.update_progress = self.__update_progress

        self.__create_form()

        self.__create_label()

        self.__create_buttons()

        self.__create_progress_bar()

#endregion

#region Public Methods

    def run(self):
        """Run the main loop.
        """

        self.__root.mainloop()

#nedregion

#region Private Methods

    def __create_form(self):

        # Create the window for GUI.
        self.__root = tk.Tk()

        # Set window name.
        self.__root.title("Zontromat ManJob")

        # Prevents resizing.
        self.__root.resizable(False, False)

        # Set window size.
        root_width = 500
        root_height = 500

        # Place the window in the center of the screen.
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (root_width/2))
        y_cordinate = int((screen_height/2) - (root_height/2))
        self.__root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        # Set window background colour.
        self.__root.configure(bg="#A37CF7")

    def __show_pop_up(self, device_configured):
        """Method to show a pop up.

        Args:
            device_configured (str): [description]
        """

        if device_configured == "sensor":
            # Shows a pop up window when a sensor is configured.
            messagebox.showinfo("Done", "Configuration of the sensor is complete. Please do a power cycle.")

        if device_configured == "power_analyzer":
            # Shows a pop up window when a power analyzer is configured.
            messagebox.showinfo("Done", "Configuration of the power analyser is complete. Please do a power cycle.")

        if device_configured == "white_island":
            # Shows a pop up window when a power analyzer is configured.
            messagebox.showinfo("Done", "Configuration of the white island is complete. Please do a power cycle.")


    def __create_label(self):

        self.__label = tk.Label(text="Which device do you want to configure?", fg="white", bg="#A37CF7")
        self.__label.config(font=("Courier", 12))
        self.__label.pack(pady=20)


    def __create_progress_bar(self):
        """Method to create a progress bar.
        """

        # Create a progress bar.
        self.__progress_bar = Progressbar(orient=HORIZONTAL, length=100, mode="indeterminate")
        self.__progress_bar.pack(expand=True)

        self.__progress_bar["value"] = 0
        self.__root.update_idletasks()

    def __update_progress(self, progress):

        # Move the progress bar.
        self.__progress_bar["value"] += progress
        self.__root.update_idletasks()


    def __create_buttons(self):

        # Button to configure the power analyzer.
        self.__btn_power_analyser = tk.Button(
            text="Power analyzer",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
            command=self.__on_click_power_analyzer)
        self.__btn_power_analyser.pack(pady=10)

        # Button to configure the upper sensor.
        self.__btn_upper_sensor = tk.Button(
            text="Upper sensor",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
            command=self.__on_click_upper_sensor)
        self.__btn_upper_sensor.pack(pady=10)

        # Button to configure the middle sensor.
        self.__btn_middle_sensor = tk.Button(
            text="Middle sensor",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
            command=self.__on_click_middle_sensor)
        self.__btn_middle_sensor.pack(pady=10)

        # Button to configure the lower sensor.
        self.__btn_lower_sensor = tk.Button(
            text="Lower sensor",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
            command=self.__on_click_lower_sensor)
        self.__btn_lower_sensor.pack(pady=10)

        # Button to configure the white island.
        self.__btn_white_island = tk.Button(
            text="White island",
            width=15,
            height=2,
            fg="white",
            bg="#6DA536",
            command=self.__on_click_white_island)
        self.__btn_white_island.pack(pady=10)

    def __enable_buttons(self):
        """Method to enable all buttons.
        """

        # Turn all buttons back to normal state.
        self.__btn_power_analyser.configure(state=NORMAL)
        self.__btn_upper_sensor.configure(state=NORMAL)
        self.__btn_middle_sensor.configure(state=NORMAL)
        self.__btn_lower_sensor.configure(state=NORMAL)
        self.__btn_white_island.configure(state=NORMAL)

    def __disable_buttons(self):
        """Method to disable all buttons.
        """

        self.__btn_power_analyser.configure(state=DISABLED)
        self.__btn_upper_sensor.configure(state=DISABLED)
        self.__btn_middle_sensor.configure(state=DISABLED)
        self.__btn_lower_sensor.configure(state=DISABLED)
        self.__btn_white_island.configure(state=DISABLED)

    def __on_config_power_analyzer(self):
        """Method to call identify, change and show pop up methods
            and enable buttons after configuration is done on button click.
        """

        # Lock the thread.
        self.__thread_lock.acquire()

        # Configure the power analyser.
        self.__programmer.config_power_analyser()

        # Show end message.
        self.__show_pop_up("power_analyser")

        # Release the thread.
        self.__thread_lock.release()

        # Enable the buttons.
        self.__enable_buttons()

    def __on_click_power_analyzer(self):
        """Power analyzer on click event method.
        """

        # Disable the buttons.
        self.__disable_buttons()

        # Start thread.
        config_power_analyzer_thread = threading.Thread(target=self.__on_config_power_analyzer, daemon=True)
        config_power_analyzer_thread.start()

    def __on_config_upper_sensor(self):
        """Method to call identify, change and show pop up methods
        and enable buttons after configuration is done on button click.
        """

        # Lock the thread.
        self.__thread_lock.acquire()

        # Configure the upper sensor.
        self.__programmer.config_upper_sensor()

        # Show end message.
        self.__show_pop_up("sensor")

        # Release the thread.
        self.__thread_lock.release()

        # Enable the buttons.
        self.__enable_buttons()

    def __on_click_upper_sensor(self):
        """Upper sensor on click event method.
        """

        # Disable the buttons.
        self.__disable_buttons()

        # Start configuration thread.
        config_upper_sensor_thread = threading.Thread(target=self.__on_config_upper_sensor, daemon=True)
        config_upper_sensor_thread.start()

    def __on_config_middle_sensor(self):
        """Method to call identify, change and show pop up methods
            and enable buttons after configuration is done on button click.
        """

        # Lock the thread.
        self.__thread_lock.acquire()

        # Configure the middle sensor.
        self.__programmer.config_middle_sensor()

        # Show end message.
        self.__show_pop_up("sensor")

        # Release the thread.
        self.__thread_lock.release()

        # Enable the buttons.
        self.__enable_buttons()

    def __on_click_middle_sensor(self):
        """Middle sensor on click event method.
        """

        # Disable the buttons.
        self.__disable_buttons()

        # Start thread.
        config_middle_sensor_thread = threading.Thread(target=self.__on_config_middle_sensor, daemon=True)
        config_middle_sensor_thread.start()

    def __on_config_lower_sensor(self):
        """Method to call identify, change and show pop up methods
            and enable buttons after configuration is done on button click.
        """

        # Lock the thread.
        self.__thread_lock.acquire()

        # Configure the lower sensor.
        self.__programmer.config_lower_sensor()

        # Show end message.
        self.__show_pop_up("sensor")

        # Release the thread.
        self.__thread_lock.release()

        # Enable the buttons.
        self.__enable_buttons()

    def __on_click_lower_sensor(self):
        """Lower sensor on click event method.
        """

        # Disable the buttons.
        self.__disable_buttons()

        # Start thread.
        config_lower_sensor_thread = threading.Thread(target=self.__on_config_lower_sensor, daemon=True)
        config_lower_sensor_thread.start()

    def __on_config_white_island(self):
        """Method to call identify, change and show pop up methods
            and enable buttons after configuration is done on button click.
        """

        # Lock the thread.
        self.__thread_lock.acquire()

        # Configure the white island.
        self.__programmer.config_upper_sensor()

        # Show end message.
        self.__show_pop_up("white_island")

        # Release the thread.
        self.__thread_lock.release()

        # Enable the buttons.
        self.__enable_buttons()

    def __on_click_white_island(self):
        """White island on click event method.
        """

        # Disable the buttons.
        self.__disable_buttons()

        # Start thread.
        config_white_island_thread = threading.Thread(target=self.__on_config_white_island, daemon=True)
        config_white_island_thread.start()

#endregion
