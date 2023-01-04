#!/usr/bin/python3

"""Write a function that adds a new attribute to an object if it`s possible:"""


def add_attribute(obj, att, value):
    """adds new attributr if possible"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att, value)
