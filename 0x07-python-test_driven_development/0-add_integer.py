#!/usr/bin/python3
"""
This module is used to add an integer.
"""
def add_integer(a, b=98):
    """
    This function adds two integers together and returns a result.
    It takes integers or floats as arguments.
    If a float passes through than it takes that argument and turns it
    into an integer.
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
