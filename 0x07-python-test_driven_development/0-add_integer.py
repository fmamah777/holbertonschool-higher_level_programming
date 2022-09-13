#!/usr/bin/python3
"""
Fuction that adds 2 integers, must be an int or float
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
"""


def add_integer(a, b=98):
    """
    add_integer - takes 2 args, must be int or float
    a: int 1
    b: int 2
    return: int: python3 -c 'print(__import__("my_module").__doc__)'
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
