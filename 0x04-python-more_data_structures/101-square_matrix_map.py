#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    '''
    The original argument is not modified
    '''
    return list(map(lambda row: (list(map(lambda x: x * x, row))), matrix))
