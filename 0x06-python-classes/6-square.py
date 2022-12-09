#!/usr/bin/python3


""" Square class"""


class Square:
    """ a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization"""
        # if not isinstance(size, int):
        #     raise TypeError("size must be an integer")
        # if size < 0:
        #     raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
