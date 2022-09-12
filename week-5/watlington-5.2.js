/* 
Title: watlington-5.2.js
Author: William Watlington
Date: 11 September 2022
Description: MongoDB Shell query demos with projection
*/

// insert new document to users collection
db.users.insertOne({firstName: "Lois", lastName: "Lane", employeeId: "3456", email: "llane@yell.com"})

// update mozart user's email address to mozart@me.com
db.users.updateOne({lastName: "mozart"}, {$set:{email: "mozart@me.com"}})

// display mozart document to confirm updated email
db.users.findOne({lastName: "Mozart"})

// list all documents in the users collection using projection to only display firstName, lastName, and email fields
db.users.find({}, {firstName: 1, lastName: 1, email:1 })