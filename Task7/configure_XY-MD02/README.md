> # This is a documentation file for configuration of XY-MD02 device:

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

* Here is a link to the documentation from the manufacturer in pdf: http://sahel.rs/media/sah/techdocs/xy-md02-manual.pdf

* The program reads the temperature and the humidity from a XY-MD02 device with those two functions:

```py
def read_temperature(unit):

    response = client.read_input_registers(
        address=1,
        count=1,
        unit=unit)

    temperature = int(response.registers[0]) / 10
    print(f"Temperature: {temperature}")
    return temperature

def read_humidity(unit):

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=unit)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")
    return humidity
```

* If you don't know the device's id or you forgot it, the identify_device_id function finds what is the device's id:

```py
def identify_device_id(begin_id=1, end_id=254):

    global client

    current_id = -1
    # for loop has range from 1 to 254, because of modbus specification.
    for index in range(begin_id, end_id):
        try:
            read_temperature(index)
            read_humidity(index)
            current_id = index
            break

        except Exception as e:
            print(f"No device found at id: {index}")

    return current_id
```

* If you have a lot of XY-MD02 devices and you want to change all of their ids the change_device_id function does it for you:

```py
def change_device_id(current_id, new_id):

    global client

    state = False

    # Only values from 1 to 254 can be passed.
    if new_id < 1 or new_id > 254:
        raise argparse.ArgumentTypeError('Invalid value! Insert 1 ~ 254.')
    else:
        response = client.write_register(0x0101, new_id, unit=current_id)
        print(response)
        state = True

    return state
```

* If you want to change the device's baudrate, you can do it with the following function:

```py
def change_devide_baudrate(current_id, new_baudrate):

    global client

    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
        raise argparse.ArgumentTypeError('Invalid value! Insert 9600, 14400 or 19200.')
    else:
        response = client.write_register(0x0102, new_baudrate, unit=current_id)
        print(response)
```

>  **If you dont pass any arguments in the terminal, the defaults are taken and written.**

---
# HELP:

> Here is a list of all the arguments that could be passed from the terminal:

* Set new device id of type **int**, default is **1**:
```sh
$ --new_id
```

* Modbus COM port of type **str**, default is **COM5**:
```sh
$ --port
```

* Rate in symbols per second of type **int**, default is **9600**:
```sh
$ --baudrate
```

* Set new device baudrate of type **int**, default is **9600**:
```sh
$ --new_baudrate
```

* Identify device's ID of type **str**, default is **False**, you should set it to True only if you want to identify the ID:
```sh
$ --identify
```

* The begin ID of the device to search from of type **int**, default is **1**:
```sh
$ --begin_id
```

* The end ID of the device to stop searching of type **int**, default is **254**:
```sh
$ --end_id
```

---
# Examples:

To run the following commands in the terminal you have to change the directory to the folder that the program is saved.

You can do that with typing **cd** and then the directory of the program in the terminal.

* Changes the device ID:
```sh
$ python main.py --new_id 2
Connected
Temperature: 28.2
Humidity: 34.6
WriteRegisterResponse 257 => 2
WriteRegisterResponse 258 => 9600
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

If you type a wrong value for example (string in that case) when trying to change the id of the device, the terminal says "invalid int value 'gosho':
```sh
$ python main.py --new_id gosho
usage: main.py [-h] [--new_id NEW_ID] [--port PORT] [--baudrate BAUDRATE] [--new_baudrate NEW_BAUDRATE] [--identify IDENTIFY]
               [--begin_id BEGIN_ID] [--end_id END_ID]
main.py: error: argument --new_id: invalid int value: 'gosho'
```

* Pass the COM port that your device is using:

In case the device is not on the given COM port:
```sh
$ python main.py --port COM3
No connection
```
In case the device is on the given COM port:
```sh
$ python main.py --port COM5
Connected
No device found at id: 1
Temperature: 28.9
Humidity: 33.0
WriteRegisterResponse 257 => 1
WriteRegisterResponse 258 => 9600
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

If you type a wrong value for example (int in that case) when trying to give the COM port of the device:

```sh
$ python main.py --port 15
No connection
```

* The baudrate that your device is using:
```sh
$ python main.py --baudrate 9600
Connected
Temperature: 29.0
Humidity: 32.0
WriteRegisterResponse 257 => 1
WriteRegisterResponse 258 => 9600
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

* Changes the baudrate of the device:
```sh
$ python main.py --new_baudrate 14400
Connected
Temperature: 29.0
Humidity: 30.9
WriteRegisterResponse 257 => 1
WriteRegisterResponse 258 => 14400
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

* Identify device's ID:
```sh
$ python main.py --identify True
Connected
Temperature: 29.0
Humidity: 31.9
Device ID: 1
$ _
```

If you type a wrong value for example (int or string different from "True") when trying to give the COM port of the device:

```sh
$ Connected
argparse.ArgumentTypeError: Invalid value! Set value to True.
$ _
```

* The begin ID of the device to search from:
```sh
$ python main.py --begin_id 1
Connected
Temperature: 29.0
Humidity: 30.3
Device ID: 1
$ _
```

* The end ID of the device to stop searching:
```sh
$ python main.py --end_id 15
Connected
Temperature: 29.0
Humidity: 30.5
Device ID: 1
$ _
```

> You can use these arguments in combinations:

* In case you want to identify device's id and search only from id 1 to 20:
```sh
$ python main.py --identify True --begin_id 1 --end_id 20
Connected
Temperature: 29.1
Humidity: 31.7
Device ID: 1
$ _
```

* In case you want to set the baudrate to 14400 and the id to 5:
```sh
$ python main.py --new_baudrate 14400 --new_id 5
Connected
Temperature: 29.1
Humidity: 31.3
WriteRegisterResponse 257 => 5
WriteRegisterResponse 258 => 14400
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

* In case you want to return the baudrate to 9600 and the device id to 1:
```sh
$ python main.py --baudrate 14400 --new_baudrate 9600 --new_id 1
Connected
No device found at id: 1
No device found at id: 2
No device found at id: 3
No device found at id: 4
Temperature: 29.1
Humidity: 32.0
WriteRegisterResponse 257 => 1
WriteRegisterResponse 258 => 9600
Ready...
Please do power cycle for the device.
Do you want a new one?: no
$ _
```

> I found misleading information in the documentation for XY-MD02 device from the manufacturer. I tryed to set the baudrate of the device to 10000 and to 38400 and it worked. In the documentation from the manufacturer there are three states that should be working: 9600, 14400, 19200 baudrate.
