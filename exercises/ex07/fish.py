"""File to define Fish class."""

__author__ = "730753182"


class Fish:
    """Make the class Fish."""

    age: int

    def __init__(self):
        """Initialize the age as 0."""
        self.age = 0
        return None

    def one_day(self):
        """Age the fish."""
        self.age += 1
        return None
