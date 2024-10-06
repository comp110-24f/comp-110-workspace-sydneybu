"""cq03 count the number of occurances of a letter in a phrase"""

__author__ = "730753182"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(phrase):
        if phrase[index] == search_char:
            count = count + 1
        index = index + 1
    print(count)
    return count
