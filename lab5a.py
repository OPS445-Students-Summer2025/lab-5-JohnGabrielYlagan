#!/usr/bin/env python3

# Author ID: jgylagan
# Lab 5a - Working with Files

# Takes file_name as string for a file name, returns its entire contents as a string
def read_file_string(file_name):
    f = open(file_name, 'r')   # r for read only    
    read_data = f.read()   # contents of file into a string                           
    return read_data    

# Takes a file_name as string for a file name, 
# return its entire contents as a list of lines without new-line characters
def read_file_list(file_name):
    f = open(file_name, 'r')
    read_data = f.read()
    list_of_lines = read_data.splitlines() # to dictate new lines
    return list_of_lines


# main block
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))