#!/usr/bin/env python3

print('Hello world')

# Section 1

## The computers "memory"

## Numbers and basic operations
print(2+1)

## Strings
print('Hello world')

## Creating variables
my_first_var = 4

my_second_var = 2+1

print(my_first_var, my_second_var)

## Lists
x = [ 1, 2, 3, 4]

print(x)

print(x[1])

print( x[0] + x[3])

## If
if True: print('goodbye')

if x[0] == 1:
    print('x[0] equals 1')

## Else
if x[0] == 2:
    print('x[0] equals 2')
else:
    print('x[0] != 2')


# Section 2

## Ints, floats, and types of variables
y = 1.24

print(type(y))
print(type(x))
print(type(x[2]))


## Variables in strings
print (f'y = {y}')
print (f'x[1] = {x[1]}')

## Booleans
z = False

print(z)

z = not z

print(z)

print(not z)

## Comparisons
if z:
    print('yes')

## Lists - add, insert, delete

mylist = ["blueberry", "strawberry", "dragonfruit", "pineapple", "apple"]

## Loops

## Ranges

## Functions
