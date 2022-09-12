""" 
Title: watlington-hobbies.js
Author: William Watlington
Date: 11 September 2022
Description: Python Conditionals/Lists/Loops assignment for WEB 335
 """

hobbies = ["reading", "gaming", "magic", "racing", "pc building"]

for hobby in hobbies:
    print(hobby)

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

for day in days:
    if day == "sunday" or day == "saturday":
        print("Today you are off. It is: " + day)
    else:
        print("Today is a work day. It is: " + day)

input("test")
  