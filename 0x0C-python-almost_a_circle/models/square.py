#!/usr/bin/python3
""" Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init a Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print attributes """
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ Side-length of this square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """ Internal method to facilitate update() """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Updates Instance attributes """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ Returns a __dict__ for this class """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
