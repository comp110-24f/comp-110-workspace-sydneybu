"""ex05- practice with lists and unit tests"""

__author__ = "730753182"


def only_evens(input: list[int]):
    """takes a list and returns a new list with only the even numbers from the original list"""
    new_list: list[int] = []
    idx: int = 0

    while idx < len(input):
        # use modulo to check if the number is even
        if input[idx] % 2 == 0:
            new_list.append(input[idx])
            idx += 1
        else:
            idx += 1

    return new_list


def sub(input: list[int], int_1: int, int_2: int):
    """generate a new list from an exisiting list between two indexes"""
    new_list: list[int] = []
    idx: int = 0
    idx_a: int = int_1

    # if the input list is empty
    if len(input) == 0:
        return new_list

    while idx < len(input):

        # if the first idx num is negative,
        # start the idx iteration at the first index of the list
        if int_1 < 0:
            idx_a = 0
        # otherwise, we start at the first idx
        else:
            idx_a = int_1

        # makes sure we stay inside the limit of the second input number
        while idx_a < int_2 and idx_a < len(input):
            new_list.append(input[idx_a])
            idx_a += 1
        return new_list


def add_at_index(input: list[int], element: int, index: int) -> None:
    """add an element at a certain index of a list"""

    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.insert(index, element)
