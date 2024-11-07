"""find and return the largest number and remove all instances of it"""

__author__ = "730753182"


def find_and_remove_max(input: list[int]) -> int:
    """find and return the largest number and remove all instances of it"""
    # idx for finding the largest num
    idx: int = 1
    # idx for removing all instances of the largest num
    remove_idx: int = 0

    if len(input) == 0:
        return -1

    largest_num: int = input[0]

    while idx < len(input):
        if input[idx] > largest_num:
            # compares the list to the current largest number
            largest_num = input[idx]
            # reassigns the largest_num to the new largest number
            idx += 1
        else:
            idx += 1
    # to remove all instances of the largest num
    while remove_idx < len(input):
        if input[remove_idx] == largest_num:
            input.pop(remove_idx)
        else:
            remove_idx += 1

    return largest_num
