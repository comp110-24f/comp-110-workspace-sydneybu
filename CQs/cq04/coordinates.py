"""take two strings and turn them into a list of  coordinates"""

__author__ = "730753182"


def get_coords(xs: str, ys: str) -> None:
    x_index: int = 0
    # first while loop to keep the x coordinate the same and
    # run through the y coordinates
    while x_index < len(xs):
        y_index: int = 0
        # moves to the next y coordinate and changes the x values
        while y_index < len(ys):
            print(f"({xs[x_index]}, {ys[y_index]})")
            y_index += 1
        x_index += 1
