#!/usr/bin/python3

'''module'''

class BaseGeometry:

    '''class'''

    def area(self):

        '''function'''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        '''function'''
        
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
