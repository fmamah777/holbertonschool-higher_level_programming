#!/usr/bin/python3
"""
Class defines a rectangle
"""


class Rectangle:
    """
    Defines a rectangle by width and height other functions change the rectangle
    """

    def __init__(self, width=0, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return("")
        string = ""
        for h in range(0, self.__height):
            for w in range(0, self.__width):
                string += "#"
            if h != self.__height - 1:
                string += "\n"
        return string

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        reutrn self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return((self.__width * 2) + (self.height * 2))
