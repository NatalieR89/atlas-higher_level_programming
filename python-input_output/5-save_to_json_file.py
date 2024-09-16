#!/usr/bin/python3
'''module'''


import json


def save_to_file(my_obj, filename):
    '''function'''
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
