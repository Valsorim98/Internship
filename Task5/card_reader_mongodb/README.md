> # This is a documentation file for Task5 card_reader_mongodb project:

The project runs from main function in main.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymongo - install with command in cmd:
```py
pip install pymongo
```

* pymodbus - install with command in cmd:
```py
pip install pymodbus
```

* pyserial - install with command in cmd:
```py
pip install pyserial
```

---

* Create a MongoDB cluster and create a new database and a collection and import database.json file in the database.

* Make a connection to the MongoDB database in tokens_base.py, in the same file I created the database and the collection. Then read the database and return the response. Insert the documents to the database from access_control.py.


* Connect to the database in MongoDB in access_control.py and **on token event iterate through the token database to check if the given token is in whitelist or blacklist** and then insert a new document in the entries collection with date and time in timestamp format, reader id, token id, token state (Access granted, Access denied, etc) and direction (entry or exit).

* Create create_read_config.py to create and read the config.ini file in Task5 card_reader_mongodb.
Create three sections in the file and set keys and values to them with the following code:

```py
write_config.add_section("Database")
write_config.set("Database","URL","mongodb+srv://user:user-pass@cluster0.jfrs3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
write_config.add_section("Card_Reader")
write_config.set("Card_Reader","Port","COM3")
write_config.set("Card_Reader","ID","1")
write_config.set("Card_Reader","Baudrate","9600")
write_config.set("Card_Reader","Bytesize","8")
write_config.set("Card_Reader","Timeout","2")
write_config.set("Card_Reader","Stopbits","1")
write_config.add_section("Controller")
write_config.set("Controller","Port","COM5")
write_config.set("Controller","ID","1")
write_config.set("Controller","Method","RTU")
write_config.set("Controller","Baudrate","9600")
write_config.set("Controller","Bytesize","8")
write_config.set("Controller","Parity","None")
write_config.set("Controller","Timeout","1")
write_config.set("Controller","Stopbits","1")
```

* After creating two new collections in the database - **whitelist and blacklist** and adding tokens in them: **id: token's code and exp_date: expiration date of the token**, read the new collections and compare if the token's code exists in the read collections. The controller works if the token's code is in whitelist and doesnt if it isnt. On token event the data is inserted as a new document in entries collection.

* Check on token event if the token is expired, if it is print "The card has expired", if it isn't expired and it's in whitelist to unlock the door.

* Add a conditional statement to check if the config.ini file is existing, if it is to read it, if it doesn't to write it and read it.
