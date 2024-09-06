#!/usr/bin/python3

'''module'''

class Square:

    '''class'''
    
    @property
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @area.setter
    def area(self):

        '''area class'''
        
        return self.__size ** 2