""" 
    Title: watlington_calculator.py
    Author: William Watlington
    Date: 9/9/2022
    Description: Python calculator app
 """
# function to add two numbers
def add(num1, num2):
    return num1 + num2

# function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

#function to divide two numbers
def divide(num1, num2):
    return num1/num2

#function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# formatted test of each above function
print("11 + 3 is " + str(add(11, 3)))
print("20 - 15 is " + str(subtract(20, 7)))
print("15 / 3 is " + str(divide(15, 3)))
print("4 * 5 is " + str(multiply(4, 5)))

#input call to stop console from closing on completion
input("finished")