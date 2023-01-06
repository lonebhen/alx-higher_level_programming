#!/usr/bin/python3

"""A student class with first name, last name and age attributes"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class to json"""
        return self.__dict__
