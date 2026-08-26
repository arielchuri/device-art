#!/usr/bin/env python3
import sys

print(sys.argv)

operator = sys.argv[1]

print(operator)

match operator:
        case '+':
                print("ok")
        case '-':
                print("subtract")
