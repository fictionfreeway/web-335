""" 
Title: watlington-usersp2.py
Author: William Watlington
Date: 21 September 2022
Description: Basic python connection to MongoDB and basic queries
"""

# import MongoDB client
from pymongo import MongoClient
import datetime


# string from MongoDB for to connect to database
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.ug54bka.mongodb.net/web33DBretryWrites=true&w=majority")

# variable for accessing the web335 database
db = client['web33DB']

# create new user document
tucker = {
    "firstName": "Tucker",
    "lastName": "Thomas",
    "employeeId": "8088",
    "email": "ttom@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# insert new user into database
db.users.insert_one(tucker)

# print newly added document
print(db.users.find_one( { "employeeId": "8088" } ))

# update newly added document's email field
db.users.update_one(
    { "employeeId": "8088" },
    {    "$set": {
            "email": "tuck.tom@me.com"
        }
    }
)

# print updated document 
print(db.users.find_one( { "employeeId": "8088" } ))

# delete the new document from the database
db.users.delete_one( { "employeeId": "8088" } )

# try finding deleted document to check that it was deleted
print(db.users.find_one( { "employeeId": "8088" } ))
