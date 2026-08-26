#!/usr/bin/env python3
import random

list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))

# welcome
userName = input("Name: ")
userPass = input("Password: ")
# check the password
if userPass == "1234":
    print("Welcome " + userName + ".")
    print("Would you like to play a game?")
else:
    for x in range(0,10):
        print("INTRUDER ALERT!")
        print("---------------")

# madlib
myNoun = input("Please enter a noun: ")

print("I was walking down the street with a " + myNoun + " on my head.")

# lucky selector
myLuckyProduct = int(input("Please enter a number between 1 and 6: "))

luckyProductList = ["Marmite",
                    "Vegimite", "Alfajores de Havana", "Agar Jelly", "Shinola", "Burma Shave"]

print(luckyProductList[myLuckyProduct - 1])

# calculator
integer1 = int( input("Please enter an integer: ") )
myOperator = input("Please enter an operator: ")
integer2 = int( input("Please enter another integer: ") )

match myOperator:
        case '+':
                print(integer1 + integer2)
        case '-':
                print(integer1 - integer2)

# The end
print("Goodbye")
