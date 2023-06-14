#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: matrix to be divided.
        div: divior to divide the matrix.
  
    Returns:
        new_matrix after dividing

    Raises: 
        TypeError: If divisor is zero.    
    """
    
    if not all(isinstance(row, list) and all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integer/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError('Each row of the matrix must have the same size')
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
