/* 
Title: watlington-6.2.js
Author: William Watlington
Date: 13 September 2022
Description: MongoDB aggregate queries
 */


// display all documents in houses
db.houses.find()

// display all documents in students
db.students.find()

// add a document to students collection
db.students.insertOne({firstName: "Ron", lastName: "Weasley", studentId: "s1020", houseId: "1007"})

// verify student "Ron Weasley" has been added
db.students.findOne({lastName: "Weasley"})

// delete student document added in last steps
db.students.deleteOne({studentId: "s1020"})

// verify student document deleted no longer exists in collection
db.students.findOne({lastName: "Weasley"})

// list students by house
db.students.aggregate([{$lookup:{from: "students", localField: "houseId", foreignField: "houseId", as:"student_houses"}}])

// list students in Gryffindor 
db.students.aggregate([{$match: { "houseId": "h1007"}}, {$lookup: {from: "students", localField: "houseId", foreignField: "houseId", as: "student_houses"}}])

// list students in house with eagle mascot 
db.houses.aggregate([{ $match: {"mascot": "Eagle"}}, {$lookup: { from: "students", localField: "houseId", foreignField: "houseId", as: "student_houses"}}])


