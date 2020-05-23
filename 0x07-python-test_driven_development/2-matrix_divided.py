#!/usr/bin/python3
"""divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix."""
    msn = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(msn)

    if len(matrix) is 0:
        raise TypeError(msn)

    length = len(matrix[0])
    for rows in matrix:
        if len(rows) != length:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for iter in row:
            if len(row) is 0:
                raise TypeError(msn)
            if type(iter) not in [int, float]:
                raise TypeError(msn)

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    new = [[round(iter / div, 2) for iter in row] for row in matrix]
    return (new)
