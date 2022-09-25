""" 
Title: watlington-userssp1.py
Author: William Watlington
Date: 13 September 2022
Description: Basic python connection to MongoDB and basic queries
"""

# import MongoDB client
from pymongo import MongoClient


# string from MongoDB for to connect to database
client = MongoClient("mongodb+srv://whatabookuser:s3cret@cluster0.ug54bka.mongodb.net/whatabookretryWrites=true&w=majority")

# variable for accessing the web335 database
db = client['web33DB']

# print all documents in users collection
for user in db.users.find( {} ):  
    print(user)

# print user document with employeeId equal to 1011
print(db.users.find_one( { "employeeId": "1011" } ))

# print user document with lastName Mozart
print(db.users.find_one( { "lastName": "Mozart" } ))