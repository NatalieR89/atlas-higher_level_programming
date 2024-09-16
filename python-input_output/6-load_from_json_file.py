#!/usr/bin/python3
'''module'''


import json


def load_from_json_file(filename):
    '''function'''
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
