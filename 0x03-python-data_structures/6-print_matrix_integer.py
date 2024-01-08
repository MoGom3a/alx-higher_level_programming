#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for ins in matrix:
        if len(ins) == 0:
            print()
    for i in range(len(ins)):
        print("{:d}".format(ins[i]), end="\n" if i is len(ins) - 1 else " ")
