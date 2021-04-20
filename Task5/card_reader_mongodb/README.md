> # This is a documentation file for Task5 card_reader_mongodb project:

The project runs from main function in main.py.

If you want to turn the relays ON you have to set the write_coils method on row 39 in io_controller.py to **True**, as following:

```py
response = self.__client.write_coils(16, [True]*4, unit=1)
```

Merge Task3 with Task1: Create a MongoDB cluster and create a new database and a collection and import database.json file in the database.

Make a connection to the MongoDB database in tokens_base.py, in the same file I created the database and the collection. Then read the database and return the response. From access_control.py insert the documents.

Get the date and time in timestamp format and the method returns timestamp format.

Create get_tokens and insert_data methods to read the tokens database and insert data as a document into the collection in the database in tokens_base.py.

Connect to the database in MongoDB in access_control.py and on token event iterate through the token database and insert a new document in the collection with date and time in timestamp format, reader id, token id, token state (Access granted, Access denied, etc) and direction (entry or exit).
