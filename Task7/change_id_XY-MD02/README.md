> # This is a documentation file for Task7:

* The project runs from main function in main.py.

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

* The program reads the temperature and the humidity from a XY-MD02 device.

* If you don't know the device's id or you forgot it, the identify_device_id method finds what is the device's id.

* If you have a lot of XY-MD02 devices and you want to change all of their ids the change_device_id method does it for you.

* If you dont pass any arguments in the terminal, the defaults are taken and written.
