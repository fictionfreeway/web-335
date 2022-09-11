
/* 
Title: watlington-4.2.js
Author: William Watlington
Date: 10 September 2022
Description: MongoDB Shell query demos
*/

// display all documents 
db.users.find()

// find user with email address "jbach@me.com"
db.users.find({"email": "jbach@me.com"})

// find user with last name Mozart
db.users.find({"lastName": "Mozart"})

// find user with first name Richard
db.users.find({"firstName": "Richard"})

// find user with employeeId of 1010
db.users.find({"employeeId": "1010"})