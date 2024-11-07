"""testing functions in list_fns file"""

from list_fns import get_first, remove_first

# command line: python -m pytest <test python file>


def test_get_first() -> None:
    assert get_first(input=["Viktorya", "Samy", "Izzi"]) == "Viktorya"

def test_remove_first() -> None:
    my_list: list[str] = ["Viktorya", "Samy", "Izzi"]
    remove_first(my_list)
    assert my_list == ["Samy", "Izzi"]
