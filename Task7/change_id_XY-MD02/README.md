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
def identify_device_id():

    global client

    current_id = -1
    # for loop has range from 1 to 254, because of modbus specification.
    for index in range(1, 254):
        try:
            read_temperature(index)
            read_humidity(index)
            print(f"Device id: {index}")
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

* If you dont pass any arguments in the terminal, the defaults are taken and written.
