#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ro in range(len(matrix)):
        for co in range(len(matrix[ro])):
            print("{:d}".format(matrix[ro][co]), end='')
            if co < len(matrix[ro]) - 1:
                print(" ", end='')
        print("".format('\n'))
