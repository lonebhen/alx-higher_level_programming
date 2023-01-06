#!/usr/bin/python3

"""Pascal`s Triangle"""


def pascal_triangle(n):
    """Pascal`s triangle"""

    list = [1]
    if n <= 0:
        return []
    else:
        for i in range(n):
            print(list)
            new_list = []
            new_list.append(list[0])
            for i in range(len(list) - 1):
                new_list.append(list[i] + list[i+1])
            new_list.append(list[-1])

            list = new_list
