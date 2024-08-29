"""calculates the number and price of tea bags and treats for a tea party"""

__author__ = "730753182"


def main_planner(guests: int) -> None:
    """takes guest input and calculates cost and number of tea bags and treats"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    """this above line really stumped me but i figured out that i needed to call tea_bags and treats
    in order to give cost values to multiply"""


def tea_bags(people: int) -> int:
    """computes the number of tea bags needed based on the number of people"""
    return people * 2


def treats(people: int) -> int:
    """number of treats needed based on the amount of tea consumed"""
    tea_bags(people)
    return people * 3


def cost(tea_count: int, treat_count: int) -> float:
    """calculates the cost of tea bags and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending?")))
