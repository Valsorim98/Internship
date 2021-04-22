> # This is a documentation file for Task6:

The task is to create a program and use the card reader and the database in MongoDB. On token event to add the token's code to the whitelist.

* The project runs from main function in main.py.

> Environment:

* This script is written in Python 3.9.2.

> Required modules to run the program:

* pymongo - install with command in cmd:
```py
pip install pymongo
```

* pyserial - install with command in cmd:
```py
pip install pyserial
```

---
* Create a new folder for Task6, main function in main.py and tokens_base.py and methods to read the database from MongoDB and insert data.

* Create card_reader.py with a constructor for the card reader and methods for card reader callback and update method to decode the token input from Ascii to string.

* Create add_token.py with constructor of the card reader instance and the tokens database.

* Create update method and card reader callback method to get input date in GMT format, convert it to timestamp format and update the database with the given token id and expiration date of the token in timestamp format in add_token.py.

* Create a method to update the given collection with a new document in tokens_base.py.

* I created two new collections in the test_db database named whitelist and blacklist and inserted new documents in both collections with id - token code and with timestamp date for the expiration date of the token.
