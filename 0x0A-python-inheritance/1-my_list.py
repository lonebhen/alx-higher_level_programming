#!/usr/bin/python3

"""A class that inherits from another(list)"""


class MyList(list):
    """My list class"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
