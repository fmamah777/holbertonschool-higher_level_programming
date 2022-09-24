#!/usr/bin/python3
"""
Contains the Rectangle* class.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class inherits from the superclass base. the attributes 
    in this class contain base width and height etc.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        
        """
        This method instantiates the object using
        initialization method from the upperclass.
        """
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """
        Getter for Rectangle width.
        """
        return self.__width

    @property
    def height(self):
        """
        this is the Getter for Rectangle height.
        """
        return self.__height

    @property
    def x(self):
        """
        Getter function for the Rectangle x.
        """
        return self.__x

    @property
    def y(self):
        """
        the Getter function for Rectangle y.
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Setter function for the Rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Setter feature for Rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        the Setter for Rectangle x.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Setter for Rectangle y.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This method returns the area of the Rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        This prints the Rectangle to stdout with the '#' char.
        """
        for lines in range(self.__y):
            print()
        for row in range(self.__height):
            for spot in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        This method returns a string representation of the
        Rectangle object.
        """
        return "[Rectangle] \
({}) {}/{} - {}/{}".format(self.id, self.__x,
                           self.__y, self.__width,
                           self.__height)

    def update(self, *args, **kwargs):
        """
        This method assigns 'args' to each attribute. In order;
        id, width, height, x, and y. Or, if there is no 'args',
        then it will use 'kwargs'.
        """
        attrnum = 0
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for arg in args:
                setattr(self, attrs[attrnum], arg)
                attrnum += 1
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        returns a verson of the Rectangle object.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
