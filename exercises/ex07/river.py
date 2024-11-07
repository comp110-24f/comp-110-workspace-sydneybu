"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730753182"


class River:
    """Create river class."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove old fish and bears."""
        # create new lists
        surviving_fish: list[Fish] = []
        surviving_bears: list[Bear] = []

        # add fish to new list
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)

        # add bears to new list
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)

        # update the old lists
        self.fish = surviving_fish
        self.bears = surviving_bears

        return None

    def bears_eating(self):
        """Bears eat if there are enough fish."""
        for bear in self.bears:
            # if there are more than 5 fish
            if len(self.fish) >= 5:
                # remove 3 fish from fish
                self.fish.pop(0)
                self.fish.pop(0)
                self.fish.pop(0)
                # call eat() to increase the bear's hunger
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove bears w a negative hunger."""
        # make a new list
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            # if their hunger is above 0
            if bear.hunger_score >= 0:
                # add them to the new list
                surviving_bears.append(bear)
        # update self.bears to be the new list
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        """A pair of fish will produce 4 fish."""
        # make a variable of the new fish that will be made
        num_new_fish = (len(self.fish) // 2) * 4
        # append new fish for the number of new fish
        for _ in range(0, num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """A pair of bears will produce 1 bear."""
        # make a variable of the number of bears that can be made
        num_new_bears = len(self.bears) // 2
        # add those bears to Bears()
        for _ in range(0, num_new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Print status of river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day seven times to model a week."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove the frontmost fish from the river a # of times."""
        for _ in range(0, amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
