#!/usr/bin/env python3

# Author ID: jgylagan
# Lab 5c - Handling ERrors


# Add two numbers together, return the result, if error return string 'error: could not add numbers'
def add(number1, number2):
    try:
        return int(number1) + int(number2)  # try convert input as ints
    except:
        return 'error: could not add numbers'

# Read a file, return a list of all lines, if error return string 'error: could not read file'
def read_file(filename):
    try:
        f = open(filename, 'r')     # open as read only
        lines = f.readlines()       
        f.close()                   
        return lines
    except:
        return 'error: could not read file'



# main block

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception