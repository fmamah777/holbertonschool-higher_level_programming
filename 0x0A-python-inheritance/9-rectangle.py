#!/usr/bin/python3
""" 9-rectangle.py creates a Rectangle from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeometry """
    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __repr__(self):
        """ Print the width/height of rectangle """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        """ Area of Rectangle """
        return self.__width * self.__height
