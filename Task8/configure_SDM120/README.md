> # This is a documentation file for configuration of SDM120 power analyzer:

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

* Here is a link to the documentation from the manufacturer in pdf: https://www.eastroneurope.com/images/uploads/products/protocol/SDM120-MODBUS_Protocol.pdf

* The program reads voltage from the analyzer with the function:

```py
def read_voltage(unit):

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
```

* If you don't know the device's id or you forgot it, the identify_device_id function finds what is the device's id:

```py
def identify_device_id(begin_id=1, end_id=247):

    global client

    current_id = -1
    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        try:
            read_voltage(index)
            current_id = index
            break

        except Exception as e:
            print(f"No device found at id: {index}")

    print(f"Device ID: {current_id}")
    return current_id
```

* If you want to change the ID of the power analyzer you can do it with the following function:

```py
def change_device_id(current_id, new_id):

    global client

    state = False

    # Pack new_id from float to bytes
    byte_value = pack("f", new_id)

    # Unpack bytes to binary
    unpack_value = unpack("<HH", byte_value)

    # Append the lower number on last position for little-endian
    regs_value = []
    regs_value.append(unpack_value[1])
    regs_value.append(unpack_value[0])

    # Write registers 20,21 with the float number
    response = client.write_registers(20, regs_value, unit=current_id)
    print(response)

    state = True

    return state
```

* If you want you can change the device baudrate with the following function:

```py
def change_devide_baudrate(current_id, new_baudrate):

    global client

    # Pack new_baudrate from float to bytes
    byte_value = pack("f", new_baudrate)

    # Unpack bytes to binary
    unpack_value = unpack("<HH", byte_value)
    
    # Append the lower number on last position for little-endian
    regs_value = []
    regs_value.append(unpack_value[1])
    regs_value.append(unpack_value[0])
    response = client.write_registers(28, regs_value, unit=current_id)
    print(response)
```

---
# HELP:

* To be able to work with the power analyzer you have to turn its power on and connect it to your computer, if you just want to read from it. But if you want to write to the power analyzer you have to push and hold the **SET** button for 2-3 seconds, then the numbers disappear and now you can see **set** on the display. Now the device is ready to be written on and you can do the changes. After the changes are made you must do a power cycle.

* The functions for changing the device ID and device baudrate will only work if the user gives a proper input (integer). For example:

* For new device ID: The numbers from 1 ~ 247.

* For new device baudrate: 0, 1, 2 or 5.

If the user gives a string input or an invalid value the program will keep asking for a proper input.

---
# Examples:

* Changes the device ID and baudrate:

```sh
$ Connected
Enter a new ID - 1 ~ 247: 1
For 2400 baud: 0,
For 4800 baud: 1,
For 9600 baud: 2,
For 1200 baud: 5.
Enter a new baudrate: 2
Voltage: 237.1
Device ID: 1
WriteMultipleRegisterResponse (20,2)
WriteMultipleRegisterResponse (28,2)
Ready...
Please do power cycle for the device.
$ _
```

If you type a wrong value for example (string in that case) when trying to change the id of the device:

```sh
$ Connected
Enter a new ID - 1 ~ 247: gosho
Invalid value! Type a number 1 ~ 247.
$ _
```

If you type a wrong value for example (string in that case) when trying to change the baudrate of the device:

```sh
$ Connected
Enter a new ID - 1 ~ 247: 1
For 2400 baud: 0,
For 4800 baud: 1,
For 9600 baud: 2,
For 1200 baud: 5.
Enter a new baudrate: chushki
Invalid value! Type a number 0, 1, 2 or 5.
For 2400 baud: 0,
For 4800 baud: 1,
For 9600 baud: 2,
For 1200 baud: 5.
Enter a new baudrate:
$ _
```
