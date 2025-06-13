#!/usr/bin/env python3

# Author ID: jgylagan
# Lab 5b - Writing to Files

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

 #part 2

# Takes two strings, appends the string to the end of the file
def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')  # a for append mode
    f.write(string_of_lines)
    f.close()  # f.close to save the file with any appends


# Takes a string and list, writes all items from list to file where each item is one line
def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')  # write mode
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()   # f.close to save written


# Takes two strings, reads data from first file, writes data to new file, adds line number to new file
def copy_file_add_line_numbers(file_name_read, file_name_write):
    f_read = open(file_name_read, 'r')   
    f_write = open(file_name_write, 'w')
    line_number = 1
    for line in f_read:
        f_write.write(f"{line_number}:{line}")
        line_number += 1
    f_read.close()
    f_write.close()


# main block
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

    '''
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
    '''