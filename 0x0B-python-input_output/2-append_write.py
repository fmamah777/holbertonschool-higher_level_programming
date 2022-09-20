#!/usr/bin/python3
""" appending a string """

def append_write(filename=""):
    """ prototype to append the end of UTF8 file """
    with open(filename, encoding='utf-8') as f:
        return f.write(filename)
