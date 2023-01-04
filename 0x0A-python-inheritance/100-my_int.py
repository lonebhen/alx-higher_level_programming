#!/usr/bin/python3

"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt inherits from `int` """

    def __eq__(self, value):
        """Overrides equals to"""
        return self.real != value

    def __ne__(self, value):
        """Overrides not equals to"""
        return self.real == value
