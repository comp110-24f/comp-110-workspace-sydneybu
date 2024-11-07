"""testing different functions"""


def get_first(input: list[str]) -> str:
    """returns the first element in the list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """pop first element off of the input list"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """returns first element and pops it off of the input list"""
    first: str = input[0]
    input.pop(0)
    # popping gets rid of the value so we want to save it as "first" so we can print that value later
    return first
