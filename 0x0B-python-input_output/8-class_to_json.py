#!/usr/bin/python3
""" From class to JSON serialization """


def class_to_json(obj):
    """
    object that will be converted to JSON then,
    return will be the JSON representation of dictionary
    """
    return obj.__dict__
