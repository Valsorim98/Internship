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

    try:
        response = client.write_register(0x0101, new_id, unit=current_id)
        print(response)
        state = True

    except Exception as e:
        print(e)

    return state
```

* If you want to change the device's baudrate, you can do it with the following function:

```py
def change_devide_baudrate(current_id, new_baudrate):

    global client

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

* Identify device's ID of type **bool**, default is **False**, you should set it to True only if you want to identify the ID:
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
$ python main.py --new_id [insert new id here]
```

* Pass the COM port that your device is using:
```sh
$ python main.py --port [insert COM port here]
```

* The baudrate that your device is using:
```sh
$ python main.py --baudrate [insert baudrate here]
```

* Changes the baudrate of the device:
```sh
$ python main.py --new_baudrate [insert new baudrate here]
```

* Identify device's ID:
```sh
$ python main.py --identify True
```

* The begin ID of the device to search from:
```sh
$ python main.py --begin_id [insert begin id here]
```

* The end ID of the device to stop searching:
```sh
$ python main.py --end_id [insert end id here]
```

> You can use these arguments in combinations:

* In case you want to identify device's id and search only from id 1 to 20:
```sh
$ python main.py --identify True --begin_id 1 --end_id 20
```

* In case you want to set the baudrate to 14400 and the id to 5:
```sh
$ python main.py --new_baudrate 14400 --new_id 5
```

* In case you want to return the baudrate to 9600 and the device id to 1:
```sh
$ python main.py --baudrate 14400 --new_baudrate 9600 --new_id 1
```

> I found misleading information in the documentation for XY-MD02 device from the manufacturer. I tryed to set the baudrate of the device to 10000 and to 38400 and it worked. In the documentation from the manufacturer there are three states that should be working: 9600, 14400, 19200 baudrate.
