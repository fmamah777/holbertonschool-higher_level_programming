#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # add 0 to tuple
    if len(tuple_a) > 2:
        tuple_a = tuple_a + (0, 0)
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0, 0)
        frstnum = tuple_a[0] + tuple_b[0]
        scndnum = tuple_a[1] + tuple_b[1]
        newtuple = (frstnum, scndnum)
        return newtuple
