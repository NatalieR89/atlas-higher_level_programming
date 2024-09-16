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

class Rectangle(BaseGeometry):

    '''class'''

    def __init__(self, width, height):

        '''function'''

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        '''function'''

        return self.__width * self.__height

    def __str__(self):

        '''function'''

        return f"[Rectangle] {self.__width}/{self.__height}"

class Square(Rectangle):

    '''class'''

    def __init__(self, size):

        '''function'''

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):

        '''function'''

        return self.__size * self.__size

    def __str__(self):

        '''function'''

        return f"[Square] {self.__size}/{self.__size}"