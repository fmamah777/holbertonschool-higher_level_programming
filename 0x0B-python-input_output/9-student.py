#!/usr/bin/python3
"""
This module contains class: Student
"""


class Student:
    """
    This class creates a Student identification object that contains; a first_name,
    last_name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        This method initializes the object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This method returns a dictionary representation of
        itself.
        """
        return self.__dict__
