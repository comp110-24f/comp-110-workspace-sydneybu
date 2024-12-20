"""File to define Bear class."""

__author__ = "730753182"


class Bear:
    """Make the class Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age the bear and decrease its hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Hunger score increases when eating."""
        # increases the hunger score by the number of fish eaten
        self.hunger_score += num_fish
        return None
