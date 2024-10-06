"""Mutating functions."""

__author__ = "730753182"


def manual_append(append_list: list[int], int: int) -> None:
    """appends a number to the end of a list"""
    append_list.append(int)


def double(double_list: list[int]) -> None:
    """multiply every item in the list by 2"""
    idx: int = 0
    while idx < len(double_list):
        double_list[idx] = double_list[idx] * 2
        # multiplies by 2 and increases index
        idx += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
