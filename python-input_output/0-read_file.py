#!/usr/bin/python3
'''
module
'''
def read_file(filename=""):
    '''
    function
    '''

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        if content:
            print(content.rstrip())