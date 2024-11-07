"""Summing the elements of a list using different loops"""

__author__ = "730753182"


def w_sum(list: list[float]) -> float:
    """calculates sum of a list using while loop"""
    # create an index variable and a sum to store the numbers in
    idx: int = 0
    sum: float = 0.0

    # so an empty list returns 0.0
    if len(list) == 0:
        return 0.0
    # while loop
    while idx < len(list):
        sum += list[idx]
        idx += 1
    return sum


def f_sum(list: list[float]) -> float:
    """calculates sum of a list using for..in loop"""
    # only need sum variable to store the numbers in
    sum: float = 0.0

    # so an empty list returns 0.0
    if len(list) == 0:
        return 0.0
    # for..in loop
    for elem in list:
        sum += elem
    return sum


def f_range_sum(list: list[float]) -> float:
    """calculates sum of a list using for..in range loop"""
    # only need sum veriable to store the numbers in
    sum: float = 0.0

    # so an empty list returns 0.0
    if len(list) == 0:
        return 0.0
    # for..in range loop
    for elem in range(len(list)):
        sum += list[elem]

    return sum
