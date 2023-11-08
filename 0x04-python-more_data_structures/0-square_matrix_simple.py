#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return list(map(lambda sub: list(map(lambda e: e**2, sub)), matrix))
