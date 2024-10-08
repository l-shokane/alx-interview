#!/usr/bin/python3
"""
Pascal's Triangle Mock Interview
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n,
    else
    Returns empty list if n <= 0
    """
    k = []
    if n <= 0:
        return k
    k = [[1]]
    for i in range(1, n):
        temp = [1]
        for j in range(len(k[i - 1]) - 1):
            temp.append(k[i - 1][j] + k[i - 1][j + 1])
        temp.append(1)
        k.append(temp)
    return k
