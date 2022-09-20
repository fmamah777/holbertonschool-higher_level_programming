#!/usr/bin/python3
"""append write funtion"""

def append_write(filename="", text=""):
    """funtion write"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(filename)
