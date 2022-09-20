#!/usr/bin/python3
""" Return an object as a json string """

import json


def from_json_string(my_str):
    """ prototype to return object as json string"""
    return json.loads(my_str)
