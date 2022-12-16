#!/usr/bin/python3

"""Locked Class"""


class LockedClass:
    """Prevent user from instantiating new class attributes"""
    __slots__ = ["first_name"]
