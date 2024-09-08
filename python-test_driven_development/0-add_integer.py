#!/usr/bin/python3

'''Module'''

def add_integer(a, b=98):

    '''function'''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b

print(add_integer(10, 20))
print(add_integer(10))
print(add_integer(10.5, 20))
print(add_integer(10, "20"))
