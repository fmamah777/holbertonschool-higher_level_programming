#!/usr/bin/python3
"""
 contains Base class.
"""
import json
import os


class Base:
    """
    base class to inherit from nb_objects. used to identidify objects
    created without an i.d. class
    """
    __nb_objects = 0

    @classmethod
    def clear(cls):
        """
        resets  nb_objects.
        """
        Base.__nb_objects = 0

    def __init__(self, id=None):
        """
        This ignores the object.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns 'list_dictionaries'.
        """
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        JSON representation of 'list_objs', to file.
        """
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs:
            for item in list_objs:
                newlist.append(cls.to_dictionary(item))
        with open(filename, "w") as file:
            file.write(cls.to_json_string(newlist))

    @staticmethod
    def from_json_string(json_string):
        """
        returns list from json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        object returns in kwargs, 'dictionary'.
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """
        returns instance 'cls'.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as file:
            newlist = cls.from_json_string(file.read())
        newobj = []
        for dict in newlist:
            newobj.append(cls.create(**dict))
        return newobj
