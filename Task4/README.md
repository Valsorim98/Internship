# **This is a documentation file for Task4**

The project runs from main function in main.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymodbus - install with command in cmd:
```py
pip install pymodbus
```
You can see the documentation for the controller in the folder Task4 - HHC-R4I4D.md. Made by **Orlin Dimitrov**.

---
> What is Modbus RTU and RS485:

**Modbus** is a data communications protocol, master/slave type, originally published by Modicon (now Schneider Electric) in 1979 for use with its programmable logic controllers (PLCs). For the task I used **HHC-R4I4D** controler with **RS485** standard for communication.

Modbus was developed for industrial applications and is popular in industrial environments and smart homes, it is openly published and free.

The Modbus protocol uses **serial port, Ethernet, or TCP/IP** as a transport layer.

Each device communicating on a Modbus is given a **unique address**. Оnly the node assigned as the **Master** may initiate a command. All other devices are **slaves** and respond to requests and commands.

Modbus supports communication to and from multiple devices connected to the same cable or Ethernet network. For example, there can be a device that measures temperature and another device to measure humidity connected to the same cable, both communicating measurements to the same computer.

Modbus RTU (Remote Terminal Unit) is used in serial communication and makes use of a compact, binary representation of the data for protocol communication. The RTU format follows the commands/data with a cyclic redundancy check checksum as an error check mechanism to ensure the reliability of data. Modbus RTU is the most common implementation available for Modbus. Modbus messages are separated by idle (silent) periods.

The **RS-485** standard allows for long cabling distances in electrically noisy environments and can support multiple devices on the same bus. RS-485 can be used with data rates up to **10 Mbit/s in a short distance**. And at lower speed for distances up to 1200 meters.

Cons of **RS-485** over **RS-232** are that it provides a communication bus and can connect multiple devices at once, and at higher speed, also has a greater range of data transmission.

> Commands:

Modbus commands can instruct a Modbus Device to:

* Change the value in one of its registers, that is written to Coil and Holding registers.

* Read an I/O port: Read data from a Discrete and Coil ports.

* Command the device to send back one or more values contained in its Coil and Holding registers.

A Modbus command contains the Modbus **address of the device** it is intended for (1 to 247). Only the addressed device will respond and act on the command, even though other devices receive it.

---
> My work on Task4:

I connected the controler to the PC via RS-485 to USB converter. Then first I installed **pymodbus** module with typing the following command in cmd: **pip install pymodbus**

* First I make a connection with the device:

```py
import pymodbus

from pymodbus.client.sync import ModbusSerialClient as ModbusClient


client = ModbusClient(method="rtu", port="COM4", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)

connection = client.connect()
```

* Then I read and write from/to the device. **Turning all relays ON/OFF** and print the outcome on the console:

Also when printing on the console I used **[:4]** after response.bits, because I worked on **four relays** from the device and I wanted to print only the first four relays.

When the **write_coils** method is **True** the relays are turned ON. If the method is set to **False**, then the relays are turned OFF.

```py
response = client.read_coils(
    address=16,
    count=4,
    unit=1)

print(response.bits[:4])

response = client.write_coils(16, [True]*4, unit=1)

response = client.read_coils(
    address=16,
    count=4,
    unit=1)

print(response.bits[:4])
```

* Then I read and write from/to the device, this time I'm **turning relays one by one ON/OFF**

This time I had trouble with the addresses of the relays when I tryed turning relays one by one ON/OFF. Also I made the mistake of first reading only one coil, when I should have read all four coils, so that I get a proper response on the console.

When writing to the first relay the address should be 16 and **every next relay's address** should be X+1, so the second relay's address is 16+1, etc.

```py
response = client.read_coils(16, count=4, unit=1)
print(response.bits[:4])

response = client.write_coil(16+2, True, unit=1)

response = client.read_coils(16, count=4, unit=1)
print(response.bits[:4])
```

For this example the write_coil method's address is set to 16+2, which is the address of the third relay. And the function is set to **True** so the third relay will turn ON.
