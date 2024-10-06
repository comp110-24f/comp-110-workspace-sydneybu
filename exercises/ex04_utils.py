"""ex04 list practice"""

__author__ = "730753182"


def all(list: list[int], num: int) -> bool:
    """return True/False if all items in a list are equal to num"""
    idx: int = 0

    if len(list) == 0:
        # False if the user inputs an empty list
        return False

    while idx < len(list):
        if list[idx] != num:
            # we can immediately exit the function and return false if even one
            # num is not equal to the num
            return False
        else:
            idx += 1
            # adds to the index so we can keep checking through the list
    return True


def max(list: list[int]) -> int:
    """returns the largest number in a list"""
    largest_num: int = list[0]
    # using this to store the largest number in
    idx: int = 1

    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
        # error if the user inputs an empty list

    while idx < len(list):
        if list[idx] > largest_num:
            # compares the list to the current largest number
            largest_num = list[idx]
            # reassigns the largest_num to the new largest number
            idx += 1
        else:
            idx += 1
    return largest_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """checks if every element at every index is equal in two lists"""
    idx: int = 0

    if len(list_1) != len(list_2):
        # if they are different lengths, they are already not equal
        return False
    while idx < len(list_1) and idx < len(list_2):
        # probably not necessary to have both len here on line 48 but just in case
        if list_1[idx] != list_2[idx]:
            return False
        else:
            idx += 1
    return True


def extend(list_1: list[int], list_2: list[int]) -> None:
    """appending one list to the end of another"""
    idx: int = 0

    while idx < len(list_2):
        # used len of list 2 because as we append to list 1, it gets longer
        # and would run through the while loop too many times if we used len(list_1)
        list_1.append(list_2[idx])
        idx += 1

    print(list_1)
    # since we're not returning anything, we print the new list
