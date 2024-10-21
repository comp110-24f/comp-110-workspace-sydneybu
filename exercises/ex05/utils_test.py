from utils import only_evens, sub, add_at_index
import pytest

"""unit tests for utils"""

__author__ = "730753182"


# only evens tests
def test_only_evens_return() -> None:
    """tests that only_evens function returns the expected value"""
    # give list, run code, check the return value
    list_1: list[int] = [0, 2, 3, 2, 5]
    assert only_evens(list_1) == [0, 2, 2]


def test_only_evens_mutate() -> None:
    """test that the only_evens function does not mutate the input list"""
    # give list, run code and then check that the list was not mutated
    list_2: list[int] = [1, 1, 3, 4, 5]
    only_evens(list_2)
    assert list_2 == [1, 1, 3, 4, 5]


def test_only_evens_edge_case() -> None:
    """test an edge case of an empty list on the only_evens function"""
    # check that the return value is []
    edge_case_list: list[int] = []
    assert only_evens(edge_case_list) == []


# sub tests
def test_sub_return() -> None:
    """tests that the sub function returns the expected value"""
    # check that the return value is as expected
    list_1: list[int] = [1, 2, 3, 4, 5]
    assert sub(list_1, 1, 4) == [2, 3, 4]


def test_sub_mutate() -> None:
    """tests that the sub function does not mutate the input list"""
    list_2: list[int] = [3, 5, 6, 7, 4, 9]
    sub(list_2, -2, 4)
    assert list_2 == [3, 5, 6, 7, 4, 9]


def test_sub_edge_case() -> None:
    """tests an edge case of a negative number on the only_evens function"""
    edge_case_list: list[int] = []
    assert sub(edge_case_list, 1, 4) == []


# add_at_index tests
def test_add_at_index_return() -> None:
    """tests that the add_at_index function returns the expected value"""
    list_1: list[int] = [2, 4, 8, 10]
    add_at_index(list_1, 6, 2)
    assert list_1 == [2, 4, 6, 8, 10]


def test_add_at_index_mutate() -> None:
    """tests that the add_at_index function does mutate the input list"""
    list_2: list[int] = [1, 3, 5, 7]
    add_at_index(list_2, 9, 4)
    assert list_2 == [1, 3, 5, 7, 9]


def test_add_at_index_edge_case() -> None:
    """tests an edge case of an empty list"""

    # explaination of this in the ex05 assignment page
    with pytest.raises(IndexError):
        add_at_index([], 2, 4)
