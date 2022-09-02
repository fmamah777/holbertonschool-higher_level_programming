#!/usr/bin/python3


def validate_index(tuple, idx):
    try:
        return tuple[idx]
    except:
        return 0


def add_tuple(tuple_a=(), tuple_b=()):
    n1 = validate_index(tuple_a, 0)
    n2 = validate_index(tuple_b, 0)

    n3 = validate_index(tuple_a, 1)
    n4 = validate_index(tuple_b, 1)
    return n1 + n2, n3 + n4
