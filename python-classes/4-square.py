#!/usr/bin/python3

'''module'''

@property
def size(self):
    return self.__size
        
@size.setter
def size(self, value):
    if not isinstance(value, int):
        raise TypeError(" size must be an interger")
    if value < 0:
        raise ValueError("size must be >= 0")
        self.__size = value

class Square:

    '''class'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size



    def area(self):

        '''area class'''
        
        return self.__size ** 2