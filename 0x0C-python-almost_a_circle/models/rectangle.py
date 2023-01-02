#!/usr/bin/python3
"""A rectangle model class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # @property
    # def width(self):
    #     return self.width

    # @width.setter
    # def width(self, value):
