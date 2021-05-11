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
    for index in range(begin_id, end_id):
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

```
