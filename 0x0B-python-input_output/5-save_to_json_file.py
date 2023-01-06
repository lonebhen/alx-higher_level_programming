#!/usr/bin/python3

"""function that writes an Object to a text file,using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write obj to file"""

    with open(filename, "w") as f:
        json.dumps(my_obj, f)
