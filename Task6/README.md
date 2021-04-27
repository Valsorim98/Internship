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
