# **Configuration of HHC-R4I4D device**

The project runs from main function in main.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymodbus - install with command in cmd:
```py
pip install pymodbus
```
You can see the documentation for the device in - HHC-R4I4D.md. Made by **Orlin Dimitrov**.

---

I connected the controler to the PC via RS-485 to USB converter. Then first I installed **pymodbus** module with typing the following command in cmd: **pip install pymodbus**

* First I make a connection with the device:

```py
import pymodbus

from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM3", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

connection = client.connect()
```

* Read coils from the device and print the outcome on the console:

Also when printing on the console I used **[:4]** after response.bits, because I worked on **four relays** from the device and I wanted to print only the first four relays.

```py
def read_coils(unit):

    global client

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])
```

* Function to identify the device ID:

```py
def identify_device_id(begin_id=1, end_id=247):

    global client

    current_id = -1
    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        try:
            read_coils(index)
            current_id = index
            break

        except Exception as e:
            print(f"No device found at id: {index}")

    return current_id
```

* Function to change device ID:

```py
def change_device_id(current_id, new_id):

    global client

    state = False

    response = client.write_register(address=2, value=1, unit=current_id)
    print(response)
    state = True

    return state
```
