#!/usr/bin/python3
'''module'''


def append_write(filename="", text=""):
    '''function'''
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
