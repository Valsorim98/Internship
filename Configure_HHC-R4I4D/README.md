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

* Make a connection with the device, read coils from it and print the outcome on the console:

Also when printing on the console I used **[:4]** after response.bits, because I worked on **four relays** from the device and I wanted to print only the first four relays.

```py
def read_coils(unit, baud_value):

    global client

    # Make a connection
    client = ModbusClient(method="rtu", port="COM3",
    timeout=0.5, stopbits=1, bytesize=8,
    parity="N", baudrate=baud_value)
    connection = client.connect()

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])
```

* Function to identify the device ID and baudrate:

```py
def identify_device_id_bd(begin_id=1, end_id=247):

    global client

    current_id = -1
    baudrate_list = [1200, 2400, 4800, 9600, 19200]
    current_id_bd = []
    time_to_stop = False

    # for loop has range from 1 to 247, because of modbus specification.
    for index in range(begin_id, end_id+1):
        if time_to_stop == True:
            break
        for baud_value in baudrate_list:
            try:
                read_coils(index, baud_value)
                current_id = index
                current_bd = baud_value
                current_id_bd.append(current_id)
                current_id_bd.append(current_bd)
                time_to_stop = True
                print(current_id_bd)
                break

            except Exception as e:
                print(f"No device found at id: {index} baudrate: {baud_value}.")

    return current_id_bd
```

* Function to change the device ID:

```py
def change_device_id(current_id, new_id):

    global client

    state = False

    # Change device ID.
    # ATTENTION: register address 1 changes the ID, mistake in the documentation(2)!
    response = client.write_register(address=1, value=6, unit=0)
    print(response)

    state = True

    return state
```

* Function to change the device baudrate:

```py
def change_device_bd(current_id, new_baudrate):

    global client

    state = False

    # Write device baudrate.
    # ATTENTION: register address 2 changes the baudrate, mistake in the documentation(3)!
    response = client.write_register(address=2, value=4, unit=0)
    print(response)

    state = True

    return state
```

> Also I found more mistakes in the documentation for the white island. The register address to change the device ID is not 2, but 1. And the register address to change the device baudrate is not 3, but 2.
