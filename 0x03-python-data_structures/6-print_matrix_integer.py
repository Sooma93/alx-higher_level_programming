#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for matrix_x in matrix:
        if len(matrix_x) == 0:
            print()
        for i in range(len(matrix_x)):
            print("{:d}".format(matrix_x[i]),
                    end="\n" if i is len(matrix_x) - 1 else " ")
