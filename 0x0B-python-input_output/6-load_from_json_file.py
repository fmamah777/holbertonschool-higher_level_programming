#!/usr/bin/python3
""" creating object from json file """
import json


def load_from_json_file(filename):
    """ prototype to load from json file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
