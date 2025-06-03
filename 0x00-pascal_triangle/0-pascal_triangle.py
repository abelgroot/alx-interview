#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Generates a Pascal's triangle.

    Args:
        n (int): Number of rows.

    Returns:
        list(list(int)): List of lists of integers representing the triangle.
    """
    triangle = list()
    if n > 0:
        for i in range(n):
            row = [1]
            for j in range(1, i + 1):
                if i != j:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
                else:
                    row.append(1)
            triangle.append(row)
    return triangle
