#!/usr/bin/python3

"""Write a function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """function to check"""

    if type(obj) == a_class:
        return True
    return False
