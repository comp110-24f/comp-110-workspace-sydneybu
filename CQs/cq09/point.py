from __future__ import annotations

"""cq09- intro to object-oriented programming"""

__author__ = "730753182"


class Point:
    # attributes
    x: float
    y: float

    # define constructor
    def __init__(self, x_init: float, y_init: float):
        """initialize point with x and y coordinates"""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """scale x and y by a given factor"""
        # update the values of x and y
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """return a new scaled Point without mutating the original"""
        # call Point with positional arguments
        return Point(self.x * factor, self.y * factor)
