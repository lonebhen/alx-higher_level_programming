#!/usr/bin/python3

"""Pascal`s Triangle"""


def pascal_triangle(n):
    """Pascal`s triangle"""

    if n <= 0:
        return []
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(tri[-1])
        triangles.append(tmp)
    return triangles
