from find_max import find_and_remove_max

"""test the max function"""

__author__ = "730753182"


def test_find_and_remove_max() -> None:
    """tests that the function returns the expected value"""
    test_list: list[int] = [6, 4, 1, 9, 9]
    assert find_and_remove_max(test_list) == 9


def test_find_and_remove_max_2() -> None:
    """test that the function mutated the list properly"""
    test_list: list[int] = [6, 4, 1, 9, 9]
    # have to run the function first, then check the list
    find_and_remove_max(test_list)
    assert test_list == [6, 4, 1]


def test_find_and_remove_max_3() -> None:
    """edge case to test an empty list input"""
    test_list: list[int] = []
    assert find_and_remove_max(test_list) == -1
