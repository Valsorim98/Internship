> # 8 March:

Learn how to **create a repo**

Learn **cd (changed directory)**
- cd "name directory" in git bash

Learn **git status, git commit, git push and git clone** in git bash

Learn how to **create ignores** with 
gitignore.io

Learn how to **add a license to a repo**

Learn how to **correct mistakes with pylist**

> # Homework:

Learn how to work with **Markdown in VSCode**

Learn **Version Control Systems (VCS)**

Learn what is **docstring** and how to use it

> # March 9:

Installed **python docstring generator extension** in VSCode (using with ctrl+shift+2)

Learned how to open pylint with cmd:
- cd Documents\Git_repos\... (directory)
- dir (shows the files in the directory)
- python -m pylint [filename] (indicates certain file)

Learned mutable (list) and immutable objects (int, float, string, tuple)

Worked on optimizing and refactoring Python tasks in PythonTasks repo

> # Homework:

What is OOP and what is it used for in Python


> # March 10:

Learn how to **create classes, methods and functions and how to call them**

> # Homework:

Finish Person.py task with **try except in a while cycle**

> # March 11:

Exercise creating classes, methods and functions and calling them

Create new file Animal.py with Animal class, constructor for animals, greet method, check_for_duplicates method and main function

> # Homework:

Finish the check_for_duplicates method

> # March 12:

Remove errors from pylint on person.py and animal.py

Learn about **override methods**

Create test_override.py to test override

Learn **how to import files**

Create two classes in separate files and import them in main.py

> # Homework:

Read about public, protected and private methods

> # March 15:

Create Task1 folder and main.py, database.json, tokens_base.py, io_controller.py, card_reader.py, access_control.py.

Create a card reader constructor and a connection to the reader.

> # March 16:

Add whitelist and blacklist lists for the cards with a code and expire date for each card in database.json.

> # March 17:

Create a method to read the input data from tokens to the card reader and convert them to a string in card_reader.py.

> # March 18:

Read the data from database.json and convert it to a dictionary in tokens_base.py.

> # March 19:

Create access control class to read the inputs from tokens to check if the given token is in whitelist or blacklist in order to unlock/lock the door.

> # March 22:

Start work on Task2

Create Project1 folder for the first project.

Create main.py for main function, student.py with a constructor for students, subject.py with a constructor for subjects and database_students.json.

> # March 23:

Create students with name, age and grade in database_students.json.

Create subjects in main.py. Ask for input grades for each student and for each subject. Save the inputs in a list for each student. Get the average grade of each student.

> # March 24:

Read the content from database_students.json and convert it to a dictionary.

Get each student's grades and save them in database_students.json.

Add conditional statements to check if the students qualify for a scholarship or not.

> # March 25:

Create Project2 folder for the second project.

Create main.py for main function and person.py with a constructor for people with name and type.

Create three people - a boss and two workers. Create flags is the person here and is everybody inside or outside.

The boss comes to work and unlocks the enter door. Ask for input who is trying to enter and when all the workers are inside the enter door is now locked.

Check if there is an emergency with a conditional statement and if there is both enter and exit doors become unlocked and the workers exit the building.

> # March 26:

Ask for input who is trying to exit if its the boss he can exit anytime, if its a worker and doesnt have at least 8 hours worked to be unable to exit. When all the workers are outside the exit door is now locked. 

> # March 29:

Start work on Task3

Install **requests** module and send HTTP requests using the **GET, POST, PUT, PATCH and DELETE methods**.

> # March 30:

Send HTTP requests to **save images** from sites.

> # March 31:

Create a database and a collection in MongoDB and save documents with the content from get requests.

> # April 1:

Write documentation for Task3

> # April 2:

Finish work on Task3

> # April 5:

Start work on Task4

**Connect smart device HHC-R4I4D** to PC. Learn how to **read and write** on it using **MODBUS-RTU communication protocol and RS485**.

Use Modbus Poll for testing.

**Turn all relays ON/OFF**. Print the response on the console.

> # April 6:

**Turn relays one by one ON/OFF**. Print the response on the console.

> # April 7:

Create documentation for Task4.

> # April 8:

Finish documentation for Task4.

> # April 9:

Finish work on Task4.

> # April 13:

Start work on Task5.

* I used **GECON TCP-508N Super Smart S8-3CN** controler and a configuration utility from the manufacturer to change the device ID address.

The device is using COM5 port, Baud Rate - 9600, ID - 1, Parity - None, Word Length - 8, Stop bits - 1, IP address:192.168.1.75, Service port:502, by default. I changed the ID address from 1 (default) to 5.

* Created main.py file to read and write coils from the controller.

* Researched modbus protocol in details - got the requests and responses by bits and use a decoder to see the function codes, id address, ip address, mac address, port of the device. 

> # April 14:

Write all the coils and read before and after writing them.

> Merge Task5 with Task1:

Using the token's input to the card reader and check if the token is whitelisted. If it is in whitelist write the pin index appropriate of the relay on the controler.

> # April 15:

Install dnspython module with the command: **pip install dnspython** in cmd.

Merge Task3 with Task1: Create a MongoDB cluster and create a new database and a collection and import database.json file in the database.

Copy all files from Task1 to a new folder in Task5: card_reader_mongodb, so I can have both project instances. Import database.json file to the new database in MongoDB and delete the python file. Delete the reading from database.json file as it is not existing anymore in tokens_base.py. 

Make a connection to the MongoDB database in tokens_base.py, in the same file I created the database and the collection. Then read the database and return the response. From access_control.py insert the documents.

> # April 19:

Get the date and time in timestamp format and the method returns timestamp format.

Create get_tokens and insert_data methods to read the tokens database and insert data as a document into the collection in the database in tokens_base.py

> # Homework

Create a new folder in Task5 with new project to read the database from MongoDB and print the token codes from whitelist.

> # April 20:

Connect to the database in MongoDB in access_control.py and on token event iterate through the token database and insert a new document in the collection with date and time in timestamp format, reader id, token id, token state (Access granted, Access denied, etc) and direction (entry or exit).

Create README files for Task1 project and Task1 test project, both Task2 projects and Task5 card_reader_mongodb project and add info for how the projects work.

Create create_config.py to create a config.ini file in Task5 card_reader_mongodb.
Create three sections in the file and set keys and values to them with the following code:

```py
write_config.add_section("Connection to database")
write_config.set("Connection to database","URL","mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
write_config.add_section("Card reader")
write_config.set("Card reader","Port","COM3")
write_config.add_section("Controller")
write_config.set("Controller","ID","1")
```

Create read_config method to read the config.ini file in create_config.py.

> # April 21:

* Start work on Task6:

The task is to create a program and use the card reader and the database in MongoDB. On token event to add the token's code to the whitelist.

---
* Create a new folder for Task6, main function in main.py and tokens_base.py and methods to read the database from MongoDB and insert data.

* Create card_reader.py with a constructor for the card reader and methods for card reader callback and update method to decode the token input from Ascii to string.

* Create add_token.py with constructor of the card reader instance and the tokens database.

* Create update method and card reader callback method to get input date in GMT format, convert it to timestamp format and update the database with the given token id and expiration date of the token in timestamp format in add_token.py.

> # April 22:

* Create a method to update the given collection with a new document in tokens_base.py.

* I created two new collections in the test_db database named whitelist and blacklist and inserted new documents in both collections with id - token code and with timestamp date for the expiration date of the token.

> # April 23:

* After creating two new collections in the database - **whitelist and blacklist** and adding tokens in them: **id: token's code and exp_date: expiration date of the token**, read the new collections and compare if the token's code exists in the read collections. The controller works if the token's code is in whitelist and doesnt if it isnt. On token event the data is inserted as a new document in entries collection.

> # April 26:

Introducing to an electric actuator controlling a valve. Model FLX-05.

> Performance parameters of the device:

* Power supply: DC24V,
* Power: 20W
* Rated current: 2A,
* Output moment: 50Nm,
* Running time: 10s
* Ambient temperature: -25C° ~ 60C°
* Nominal temperature: -15C° ~ 85C°
* Protection level: IP67,
* Rotation angle: 0-360°
* Installation angle: Any angle

---
Manual testing to open/close the valve with a hexagram provided by the manufacturer. Opened the lid leading to the electrical system with a hexagram number 3. Introduction to the functions of the relays according to the documentation of the manufacturer.

> Wiring method:

* When terminal 1 links to power supply positive pole, terminal 2 links to the power supply negative pole, and that is "ON" operation.

* When terminal 1 links to power supply negative pole, terminal 2 links to the power supply positive pole, and that is "OFF" operation.

* Terminal 4 is power-less contact point common terminal.

* When "ON" runs in place, the terminal 5 outputs "full-open signal".

* When "OFF" runs in place, the terminal 6 outputs "full-shut signal".

---
Supplying current to the circuit and current measurement with a digital multimeter.

> # April 27:

* I inserted new tokens in the whitelist and blacklist collections and added loops to check on token event if the token already exists in one of the collections and if it does to ask the user for input if he wants to delete it from that collection and insert it to the other one, with answer "yes/no". With the following code:

```py
# Iterate through blacklist collection
for item in blacklist:
    db_card_id = item["_id"]
    if db_card_id == card_id:
        print("The token already exists in the blacklist collection.")
        question = input("Do you want me to delete it from blacklist and transfer it to whitelist?: ")
        if question == "yes":
            # Delete the document from blacklist
            db.blacklist.delete_one(item)
            # Insert the document in whitelist
            db.whitelist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
        if question == "no":
            break

# Iterate through whitelist collection
for item in whitelist:
    db_card_id = item["_id"]
    if db_card_id == card_id:
        print("The token already exists in the whitelist collection.")
        question = input("Do you want me to delete it from whitelist and transfer it to blacklist?: ")
        if question == "yes":
            # Delete the document from whitelist
            db.whitelist.delete_one(item)
            # Insert the document in blacklist
            db.blacklist.update_one({'_id': card_id}, {"$set": data}, upsert=True)
        if question == "no":
            break
```

> # April 28:

* Check on token event if the token is expired, if it is print "The card has expired", if it isn't expired and it's in whitelist to unlock the door in access_control.py.

* Delete unused and unnecessary code from Task5 card_reader_mongodb project. Change the directory of creation of config.ini file. Add comments and docstrings.

* Add a conditional statement to check if the config.ini file is existing, if it is to read it, if it doesn't to write it and read it.

* Update the documentation of Task5 card_reader_mongodb project with the latest work.

> # April 29:

* I was given 4 XY-MD02 devices and I created a program that reads the temperature and the humidity from a XY-MD02 device. Also changes the device ID and baudrate with arguments passed from the terminal. The program reads the temperature and humidity with the following code:

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

* If you dont pass any arguments in the terminal, the defaults are taken and written.

> # May 5:

* If you want to change the device's baudrate, you can do it with the following function:

```py
def change_devide_baudrate(current_id, new_baudrate):

    global client

    response = client.write_register(0x0102, new_baudrate, unit=current_id)
    print(response)
```

> # May 10:

* I was given a **SDM120 power analyzer** and I created a program that reads the voltage from it. Also identifies and changes the device ID and baudrate with inputs from the user. 
---
* The program reads the voltage with the following code:

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

* The program identifies the device ID with the following code:

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

> # April 11:

* The following function changes the device ID:

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

* The following function changes the device baudrate:

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

> # April 12:

* Created a new folder Configure_HHC-R4I4D in Work with main.py file for the main function. Added functions to read coils, identify and change device ID.

* Read coils function:

```py
def read_coils(unit):

    global client

    response = client.read_coils(
        address=16,
        count=4,
        unit=unit)

    print(response.bits[:4])
```

* Identify device ID function:

```py
def identify_device_id(begin_id=1, end_id=247):
    """Function to identify device's id.

    Returns:
        int: Returns current device's id as a number.
    """

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

* Change device ID function:

```py
def change_device_id(current_id, new_id):
    """Function to change the device id.

    Args:
        current_id (int): Current device id.
        new_id (int): Set new device id.

    Returns:
        bool : True if successful, else False.
    """

    global client

    state = False

    response = client.write_register(address=2, value=1, unit=current_id)
    print(response)
    state = True

    return state
```

> # April 13:

* Removed omissions from configure_HHC-R4I4D.

* Add checks if the user input is a string for new device ID and new device baudrate in Task8.

* Create a device_identification folder with a README file. It contains each usable device's name and history of ID and baudrate changing, with date of change and the person who changed it.

* Finished documentation for power analyzer (See in Task8 -> README).

> # April 14:

* Added documentation for configure_HHC-R4I4D project.

* Created a function to **identify the device's ID and baudrate** at the same time and updated the documentation in Task7.

> # April 17:

* Learning how to decode barcodes from images and from a live video from the camera.

> # April 18:

* Made a barcode with an online generator: https://barcode.tec-it.com/en/?data=Donkger%2FXY-MD02%2F9600%2F1

* Saved the barcode in .png format with 670x230 dimensions, created a bigger blank white image for a background with 400x900 dimensions in python, placed the image with the barcode on top of the white background and decoded it with opencv and python.

> # April 19:

* Created main.py with function to decode barcodes from a live video from the camera. It prints the barcode data and the barcode type.

* Merged Task7 with Task9 in a new project - barcode_decode_XY-MD02.

* Created documentation for Task9 (video_read_barcode) and barcode_decode_XY-MD02.

> # April 20:

* Created a program in configure_from_barcode.py in device_factory folder to decode a given barcode from live video and read and configure from/to the device that was read.

> # April 21:

* Process the barcode data string, identify the connected device, check for valid user inputs and if the user wants to configure the sensor's ID and baudrate.

> # April 25:

* Add function to read the voltage from the power analyzer in configure_from_barcode.py project in device factory.

* Created gui_config.py for a new project. Create a GUI for the user to work with and to read and configure the connected device.

* Created a config.ini file with default values for ID, baudrate and port for the devices.

> # April 26:

* Added functions to identify and change the sensor's ID and baudrate, read the config file and pass device's id and baudrate as arguments for new ID and baudrate.

* Refactored the project in configure_HHC-R4I4D. Changed the ID to 6 and baudrate to 9600 of the white island.

> # April 27:

* Added functions to read the voltage, identify and change the ID and baudrate of the power analyzer.

* Added functions to read the coils, identify and change the ID and baudrate of the white island.

* Updated the config file in gui_configure project.

* Pass the COM port that was read from the config file as argument to the functions for reading from the devices.

* Centralise the tkinter window on the screen.

* Added a function to display a pop up window when a device is configured from the GUI.

> # April 28:

* Append the ID and baudrate to a dict from every identify function and pass the current id as an argument to every change function, show the pop up only when the configuration is done.

* Created a documentation for gui_configure project.

* Added spacers between the label and the buttons and add a font and size of the label text.

* Combined read_temperature and read_humidity functions in one function - read_sensor_parameters and created functions create_gui and read_config.

* Refactoring, added imports and functions for disabling and enabling all the buttons and renamed gui_config.py to main.py.

> # April 31:

* Added a function in a new thread to create a progess bar, when configuration is done to destroy the progress bar and its thread.

* Updated the config file and the keys of the read lines from the config file in main function.

* Refactored progress_bar function, removed the thread and combined the progress_bar function with the identify functions.

> # June 1:

* Created a dict with the configured device and pass it as argument to show_pop_up function.

* Added voltage, coils_status and room_temp_humidity to global.

* Read about threads and python threads, daemon - a thread that is terminated on program exit.

* Make every on_config thread a daemon.
