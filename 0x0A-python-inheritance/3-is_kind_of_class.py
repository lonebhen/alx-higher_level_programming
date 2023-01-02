#!/usr/bin/python3

"""Check if two objs are instances"""


def is_kind_of_class(obj, a_class):
    """Function to check"""

    if isinstance(obj, a_class):
        return True
    return False
