> # Documentation for device_factory project:

* The project runs from main function in main.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymodbus - install with command in cmd:
```py
pip install pymodbus
```

* opencv-python - install with command in cmd:
```py
pip install opencv-python
```

* pyzbar - install with command in cmd:
```py
pip install pyzbar
```

> HELP:

* To avoid decoding errors the barcode should be maximum 10 cm away from the camera.

* In order for the program to work correctly, after changing any of the device's settings you should make a new up-to-date barcode and use it on the next run of the program.

---
* The following function read the temperature from an XY-MD02 sensor:

```py
def read_temperature(id):

    global client

    response = client.read_input_registers(
        address=1,
        count=1,
        unit=id)

    temperature = int(response.registers[0]) / 10
    print(f"Temperature: {temperature}")

    return temperature
```

* The following function read the humidity from an XY-MD02 sensor:

```py
def read_humidity(id):

    global client

    response = client.read_input_registers(
        address=2,
        count=1,
        unit=id)

    humidity = int(response.registers[0]) / 10
    print(f"Humidity: {humidity}")

    return humidity
```

* The following function changes the sensor's ID:

```py
def change_sensor_id(id, new_id):

    global client

    state = False

    # Only values from 1 to 247 can be passed.
    if new_id < 1 or new_id > 247:
        print('Invalid value! Insert 1 ~ 247.')
        return
    else:
        response = client.write_register(0x0101, new_id, unit=id)
        print(response)
        state = True

    return state
```

* The following function changes the sensor's baudrate:

```py
def change_sensor_baudrate(id, new_baudrate):

    global client

    # Only values equal to 9600, 14400 or 19200 can be passed.
    if new_baudrate != 9600 and new_baudrate != 14400 and new_baudrate != 19200:
        print("Invalid value! Insert 9600, 14400 or 19200.")
        return
    else:
        response = client.write_register(0x0102, new_baudrate, unit=id)
        print(response)
        state = True

    return state
```

* The following function creates a configuration for the used device from the decoded barcode:

```py
def create_configuration(barcode_data):

    device_configuration = []

    # Split the string data.
    bc_data_split = barcode_data.split("/")

    # Get vendor.
    vendor = bc_data_split[0]

    # Get model.
    model = bc_data_split[1]

    # Sleep for two seconds after a barcode is given
    time.sleep(2)

    # Check which barcode is given
    if vendor == "DONKGER" and model == "XY-MD02":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 9600 and\
             baudrate_value != 14400 and\
              baudrate_value != 19200:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("sensor")

    elif vendor == "EASTRON" and model == "SDM120":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 1200 and\
             baudrate_value != 2400 and\
              baudrate_value != 4800 and\
              baudrate_value != 9600:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("power_analyzer")

    elif vendor == "MAINLAND" and model == "HHC-R4I4D":

        id_value = int(bc_data_split[3])
        if id_value < 1 or id_value > 247:
            print("Invalid ID number! Insert a valid barcode.")

        baudrate_value = int(bc_data_split[2])
        if baudrate_value != 1200 and\
             baudrate_value != 2400 and\
              baudrate_value != 4800 and\
              baudrate_value != 9600 and\
              baudrate_value != 19200:
            print("Invalid baudrate! Insert a valid barcode.")

        # If the list is empty to append with id and baudrate
        if not device_configuration:
            device_configuration.append(id_value)
            device_configuration.append(baudrate_value)
            device_configuration.append("white_island")

    else:
        print("Not supported device.")

    return device_configuration
```

* The following function decodes the given barcode:

```py
def decode_barcode():

    device_configuration = []

    # Capture video
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # Make a window with these dimensions
    cap.set(3, 640) # 3 Width, 640 pixels
    cap.set(4, 480) # 4 Height, 480 pixels

    camera = True
    while camera == True:
        success, frame = cap.read()

        # Decode the barcode
        for barcode in pyzbar.decode(frame):

            barcode_data = barcode.data.decode('utf-8')

            print("Barcode type: {}; content: {}".format(barcode.type, barcode_data))

            # Hardcode value for the test.
            if barcode_data == "8782740138107":
                barcode_data = "Donkger/XY-MD02/9600/2"

            # Trim leading and trailing whitespaces in the string.
            barcode_data = barcode_data.replace(" ", "")
            barcode_data = barcode_data.replace("\r", "")
            barcode_data = barcode_data.replace("\n", "")
            barcode_data = barcode_data.replace("\t", "")
            barcode_data = barcode_data.upper()

            device_configuration = create_configuration(barcode_data)

            camera = False

        # Shows the window
        cv2.imshow("Video capture", frame)
        cv2.waitKey(1)

    return device_configuration
```

* The following function configurates the connected device:

> # TO BE CONTINUED!!!

---
> Examples:

* For the examples I'm using an XY-MD02 sensor with ID 2 and 9600 baudrate.

* If you just want to read the temperature and humidity from the device:

```sh
$ Barcode type: Code-128; content: Donkger/XY-MD02/9600/2
Connected
No device found at id: 1.
Temperature: 24.5
Humidity: 50.1
The ID of the sensor is 2.
The baudrate of the sensor is 9600.
Do you want to change the sensor ID or baudrate?: no
$ _
```

* If you want to change the ID to 3:

```sh
$ Barcode type: Code-128; content: Donkger/XY-MD02/9600/2
Connected
No device found at id: 1.
Temperature: 24.5
Humidity: 49.7
The ID of the sensor is 2.
The baudrate of the sensor is 9600.
Do you want to change the sensor ID or baudrate?: id
Enter a new ID 1 ~ 247: 3
WriteRegisterResponse 257 => 3
Sensor ID changed.
Do you want to change the sensor baudrate?: no
Ready...
Please do power cycle for the device.
$ _
```

* If you want to change the baudrate only:

```sh
$ Barcode type: Code-128; content: Donkger/XY-MD02/9600/2

$ _
```

* If you want to change ID and baudrate:

```sh
$ Barcode type: Code-128; content: Donkger/XY-MD02/9600/2

$ _
```
