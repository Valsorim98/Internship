> # This is documentation file for Task5:

The project runs from main function in main.py.

I was given a **GECON TCP-508N Super Smart S8-3CN** controller.

The task is to change the ID address of the controller.

* I used the controller and a configuration utility (from link:http://bends.se/?page=notebook/hardware/gecon-tcp-508n) from the manufacturer to change the device ID address.

The device is using COM5 port, Baud Rate - 9600, ID - 1, Parity - None, Word Length - 8, Stop bits - 1, IP address:192.168.1.75, Service port:502, by default. I changed the ID address from 1 (default) to 5 using RS485 and returned it to 1 again.

* Created main.py file to read and write coils from the controller.

> Researching modbus protocol in details.
