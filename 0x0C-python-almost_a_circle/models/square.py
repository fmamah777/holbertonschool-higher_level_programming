#!/usr/bin/python3
""" class for square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class inherits from rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Init/initialize  square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ function prints attributes """
        return '[{}] ({}) {}/{} - {}'.format(
            type(self).__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """ square side length """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """ update method () """
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """ Updates Instance """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """ __dict__ in return """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
