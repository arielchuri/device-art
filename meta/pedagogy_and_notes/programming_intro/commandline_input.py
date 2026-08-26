#!/usr/bin/env python3

operator = input("Please enter a math operator: ")

print(operator)

match operator:
        case '+':
                print("add")
        case '-':
                print("subtract")

integer1 = int( input("Please enter an integer: ") )

print( integer1 + 12)

print("Goodbye")