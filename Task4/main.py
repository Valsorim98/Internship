#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

client = ModbusClient(method="rtu", port="COM4", timeout=1, stopbits=1, bytesize=8, parity="N", baudrate=9600)
connection = client.connect()
print(connection)

while True:

    status = client.read_coils(address=0x01, starting_address=0x0011, coil_quantity=0x0004, unit=1)
    print(status)


    # turn one coil on
    #status = client.write_coil(address=0x01, function_code=0x05, unit=1)
    #print(status)
