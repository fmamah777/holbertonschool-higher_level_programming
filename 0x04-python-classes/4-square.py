#!/usr/bin/python3
"""Class Square defined"""


class Square:
    """class square defined"""
    def ___intit(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            sef.__size = value

        def my_print(self):
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    for i in range(self.__size):
                        print('#', end="")
                    print()
