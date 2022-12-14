#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes/ init  Rectangle() """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ Prints Rectangle() """
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def integer_validator(self, name, value):
        """ Validator """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0 and name in ['width', 'height']:
            raise ValueError('{} must be > 0'.format(name))
        if value < 0 and name in ['x', 'y']:
            raise ValueError('{} must be >= 0'.format(name))

    @property
    def width(self):
        """  method gets the  width """
        return self.__width

    @width.setter
    def width(self, value):
        """ method sets the width """
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """  method get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ function sets the height """
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """ this function is to get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ this function is to set x """
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """ this method is to get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ method to set y """
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """ method used to get Area """
        return self.__width * self.__height

    def display(self):
        """ method to display rectangle """
        print('\n' * self.__y + (' ' * self.__x + '#' * self.__width + '\n') *
              self.__height, end='')

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """ method performs update() """
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """  attributes are updated """
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ creates a dictionary of a class """
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
