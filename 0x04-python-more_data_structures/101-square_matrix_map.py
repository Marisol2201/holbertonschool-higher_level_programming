#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new = [list(map(lambda x: x * x, row)) for row in matrix]
    return new
