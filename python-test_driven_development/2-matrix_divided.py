#!/usr/bin/python3

def matrix_divided(matrix, div):
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
        if div == 0:
            raise ZeroDivisionError("division by zero")
    
        new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return new_matrix
