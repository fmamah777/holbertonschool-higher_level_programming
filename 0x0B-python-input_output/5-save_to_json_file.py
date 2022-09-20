#!/usr/bin/python3
""" saving to sjson file """

import json

def save_to_json_file(my_obj, filename):
    """ prototype for saving object to file with json """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
