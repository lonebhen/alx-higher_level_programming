#!/usr/bin/python3

"""Appending text to end of a file"""


def append_write(filename="", text=""):
    """append text"""
    """returns number of characters"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
