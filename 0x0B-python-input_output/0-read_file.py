#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding='UTF-8') as f:
        print(f.read(), end="")
