#!/usr/bin/python3

"""function that returns True if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """Fuction to check"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
