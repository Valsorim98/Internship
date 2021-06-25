#!/usr/bin/env python3
# -*- coding: utf8 -*-

import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Progressbar

from programmer import Programmer

class View():
    """Class View.
    """

    def __init__(self, configure):
        """Constructor for View class.
        """

        global power_analyzer, upper_sensor, middle_sensor, lower_sensor, white_island, root

        global on_click_power_analyzer, on_click_upper_sensor,\
                on_click_middle_sensor, on_click_lower_sensor, on_click_white_island

        # Instance of Programmer() class
        self.configure = configure

        # Call on_click methods from Programmer class.
        on_click_power_analyzer = self.configure.on_click_power_analyzer()
        on_click_upper_sensor = self.configure.on_click_upper_sensor()
        on_click_middle_sensor = self.configure.on_click_middle_sensor()
        on_click_lower_sensor = self.configure.on_click_lower_sensor()
        on_click_white_island = self.configure.on_click_white_island()

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


        # # Call Programmer class.
        # configure = Programmer()


    def create_progress_bar(self):
        """Method to create a progress bar.
        """

        global pb

        # Create a progress bar.
        pb = Progressbar(orient=HORIZONTAL, length=100, mode='indeterminate')
        pb.pack(expand=True)

        pb['value'] = 0
        root.update_idletasks()

        return [pb, root]

    def show_pop_up(self, device_configured):
        """Method to show a pop up.
        """

        # Call methods from Programmer() class.
        room_temp_humid = self.configure.read_sensor_parameters()
        voltage = self.configure.read_voltage()
        coils_status = self.configure.identify_white_island_id_bd()

        if device_configured["device"] == "sensor":
            # Shows a pop up window when a sensor is configured.
            messagebox.showinfo('Done', 'Configuration complete. Please do a power cycle.\n\
            Temperature: {}C°, Humidity: {}%\n'.format(room_temp_humid["temperature"], room_temp_humid["humidity"]))

        if device_configured["device"] == "power_analyzer":
            # Shows a pop up window when a power analyzer is configured.
            messagebox.showinfo('Done', 'Configuration complete. Please do a power cycle.\nVoltage: {}V'.format(voltage))

        if device_configured["device"] == "white_island":
            # Shows a pop up window when a power analyzer is configured.
            messagebox.showinfo('Done', 'Configuration complete. Please do a power cycle.\n\
            Coils status: {}'.format(coils_status))

    def enable_buttons(self):
        """Method to enable all buttons.
        """

        # Turn all buttons back to normal state.
        power_analyzer.configure(state=NORMAL)
        upper_sensor.configure(state=NORMAL)
        middle_sensor.configure(state=NORMAL)
        lower_sensor.configure(state=NORMAL)
        white_island.configure(state=NORMAL)

    def disable_buttons(self):
        """Method to disable all buttons.
        """

        power_analyzer.configure(state=DISABLED)
        upper_sensor.configure(state=DISABLED)
        middle_sensor.configure(state=DISABLED)
        lower_sensor.configure(state=DISABLED)
        white_island.configure(state=DISABLED)

    # def create_gui(self):
    #     """Method to create GUI form.
    #     """

        # global power_analyzer, upper_sensor, middle_sensor, lower_sensor, white_island, root

        # # Create the window for GUI.
        # root = tk.Tk()

        # # Set window name.
        # root.title("Configuration")

        # # Prevents resizing.
        # root.resizable(False, False)

        # # Set window size.
        # root_width = 500
        # root_height = 500

        # # Place the window in the center of the screen.
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # x_cordinate = int((screen_width/2) - (root_width/2))
        # y_cordinate = int((screen_height/2) - (root_height/2))
        # root.geometry("{}x{}+{}+{}".format(root_width, root_height, x_cordinate, y_cordinate))

        # # Set window background colour.
        # root.configure(bg='#A37CF7')

        # label = tk.Label(text="Which device do you want to configure?", fg="white", bg="#A37CF7")
        # label.config(font=("Courier", 12))
        # label.pack(pady=20)

        # # Button to configure the power analyzer.
        # power_analyzer = tk.Button(
        #     text="Power analyzer",
        #     width=15,
        #     height=2,
        #     fg="white",
        #     bg="#6DA536",
        #     command=on_click_power_analyzer)

        # power_analyzer.pack(pady=10)

        # # Button to configure the upper sensor.
        # upper_sensor = tk.Button(
        #     text="Upper sensor",
        #     width=15,
        #     height=2,
        #     fg="white",
        #     bg="#6DA536",
        #     command=on_click_upper_sensor)

        # upper_sensor.pack(pady=10)

        # # Button to configure the middle sensor.
        # middle_sensor = tk.Button(
        #     text="Middle sensor",
        #     width=15,
        #     height=2,
        #     fg="white",
        #     bg="#6DA536",
        #     command=on_click_middle_sensor)

        # middle_sensor.pack(pady=10)

        # # Button to configure the lower sensor.
        # lower_sensor = tk.Button(
        #     text="Lower sensor",
        #     width=15,
        #     height=2,
        #     fg="white",
        #     bg="#6DA536",
        #     command=on_click_lower_sensor)

        # lower_sensor.pack(pady=10)

        # # Button to configure the white island.
        # white_island = tk.Button(
        #     text="White island",
        #     width=15,
        #     height=2,
        #     fg="white",
        #     bg="#6DA536",
        #     command=on_click_white_island)

        # white_island.pack(pady=10)

        # root.mainloop()
