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

Work on Task3

Send HTTP requests to **save images** from sites.

> # March 31:

Work on Task3

Create a database and a collection in MongoDB and save documents with the content from get requests.

> # April 1:

Work on Task3

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

* Created main.py file to read coils from the controller.

* Researched modbus protocol in details - got the requests and responses by bits and use a decoder to see the function codes, id address, ip address, mac address, port of the device. 

> # April 14:

Write all the coils and read before and after writing them.
