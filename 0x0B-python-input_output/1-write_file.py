#!/usr/bin/python3

"""file writing"""


def write_file(filename="", text=""):
    """Write action"""
    """Returns the number of characters"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
