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
