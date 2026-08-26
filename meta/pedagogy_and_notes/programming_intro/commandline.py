#!/usr/bin/env python3
import sys

print(sys.argv)

print("hello, world.")

fred = 10

print(fred)

if fred > 5:
    print("Fred is greater than 5.")

mylist = ["banana", "3", "4", 5, 2, fred]

print(mylist[1])

print(1+2)

print(mylist[3] + mylist[4])

for x in mylist:
    print(x)

print("Goodbye.")
