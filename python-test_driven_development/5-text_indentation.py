#!/usr/bin/python3

'''module'''

def text_indentation(text):

    '''function'''

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    
    print("\n".join(line.strip() for line in result.split("\n")))
