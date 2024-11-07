from exercises.ex07.river import River

"""Test our code functionality."""

__author__ = "730753182"

# construct new river
my_river: River = River(10, 2)

# print out the river status
my_river.view_river()

# check one_river_week
my_river.one_river_week()
