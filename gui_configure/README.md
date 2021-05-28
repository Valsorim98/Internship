> # Documentation for gui_configure project:

* The project runs from main function in gui_config.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymodbus - install with command in cmd:
```py
pip install pymodbus
```

* argparse - install with command in cmd:
```py
pip install argparse
```

* tkinter - install with command in cmd:
```py
pip install tk
```

* configparser - install with command in cmd:
```py
pip install configparser
```

> The program identifies and configures the connected device's ID and baudrate if the connected device matches the button for it. For example if you connected a power analyzer and try to configure it as a sensor you wont be able to. The program wont be able to identify and configure the connected device. But if you connected a power analyzer and try to configure it as a power analyzer it will work.

> ATTENTION: After every device configuration you must do a power cycle.

> # HELP:

* If you want to write to the power analyzer you have to push and hold the **SET** button for 2-3 seconds, then the numbers disappear and now you can see **set** on the display. Now the device is ready to be written on and you can do the changes. After the changes are made you must do a power cycle.

> # EXAMPLES:

* When you want to configure the **power analyzer**:

Connect the power analyzer to the computer and start the program. Then click the button "Power analyzer". For the example I am using the power analyzer with ID 2 and baudrate 9600.

```sh
$ No device found at id: 1 baudrate: 1200.
No device found at id: 1 baudrate: 2400.
No device found at id: 1 baudrate: 4800.
No device found at id: 1 baudrate: 9600.
No device found at id: 2 baudrate: 1200.
No device found at id: 2 baudrate: 2400.
No device found at id: 2 baudrate: 4800.
Voltage: 238.5
{'id': 2, 'baudrate': 9600}
WriteMultipleRegisterResponse (20,2)
WriteMultipleRegisterResponse (28,2)
Please do power cycle for the device.
$ _
```

* When you want to configure the **upper sensor**:

Connect the upper sensor to the computer and start the program. Then click the button "Upper sensor". For the example I am using the upper sensor with ID 3 and baudrate 9600.

I wont show examples with the middle and lower sensors, as they are identical with the upper sensor example.

```sh
$ No device found at id: 1 baudrate: 9600.
No device found at id: 1 baudrate: 14400.
No device found at id: 1 baudrate: 19200.
No device found at id: 2 baudrate: 9600.
No device found at id: 2 baudrate: 14400.
No device found at id: 2 baudrate: 19200.
Temperature: 27.6
Humidity: 48.1
{'id': 3, 'baudrate': 9600}
WriteRegisterResponse 257 => 3
WriteRegisterResponse 258 => 9600
Please do power cycle for the device.
$ _
```

* When you want to configure the **white island**:

Connect the white island to the computer and start the program. Then click the button "White island". For the example I am using the white island with ID 6 and baudrate 9600.

```sh
$ No device found at id: 1 baudrate: 1200.
No device found at id: 1 baudrate: 2400.
No device found at id: 1 baudrate: 4800.
No device found at id: 1 baudrate: 9600.
No device found at id: 1 baudrate: 19200.
No device found at id: 2 baudrate: 1200.
No device found at id: 2 baudrate: 2400.
No device found at id: 2 baudrate: 4800.
No device found at id: 2 baudrate: 9600.
No device found at id: 2 baudrate: 19200.
No device found at id: 3 baudrate: 1200.
No device found at id: 3 baudrate: 2400.
No device found at id: 3 baudrate: 4800.
No device found at id: 3 baudrate: 9600.
No device found at id: 3 baudrate: 19200.
No device found at id: 4 baudrate: 1200.
No device found at id: 4 baudrate: 2400.
No device found at id: 4 baudrate: 4800.
No device found at id: 4 baudrate: 9600.
No device found at id: 4 baudrate: 19200.
No device found at id: 5 baudrate: 1200.
No device found at id: 5 baudrate: 2400.
No device found at id: 5 baudrate: 4800.
No device found at id: 5 baudrate: 9600.
No device found at id: 5 baudrate: 19200.
No device found at id: 6 baudrate: 1200.
No device found at id: 6 baudrate: 2400.
No device found at id: 6 baudrate: 4800.
[False, False, False, False]
{'id': 6, 'baudrate': 9600}
WriteRegisterResponse 1 => 6
WriteRegisterResponse 2 => 4
Please do a power cycle for the device.
$ _
```
