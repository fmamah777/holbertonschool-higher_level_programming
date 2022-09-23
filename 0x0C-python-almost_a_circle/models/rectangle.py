#!/usr/bin/python3

"""
This class is for rectangle
"""
from models.base import Base
class Rectangle(Base):

    """ This class inherits base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ this defines the rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
