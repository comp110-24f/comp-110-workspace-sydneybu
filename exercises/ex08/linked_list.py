"""Practice with recursive structures."""

from __future__ import annotations

# lets us refer to Node from the Node class definition


class Node:
    """Defining class Node."""

    # attributes
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializer function."""
        self.value = val
        self.next = next

    # magic method!! double underscore = automatic funtion call
    def __str__(self) -> str:
        """Magic method to make a linked list w/ arrows."""
        rest: str = ""
        if self.next is None:  # base case
            rest = "None"
        else:
            rest = str(self.next)  # calls the function again w the next node
        return f"{self.value} -> {rest}"


def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node at the given index."""
    # base case of empty list
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    # base case of correct index
    if index == 0:
        return head.value

    # move to the next node
    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return maximum data value in the linked list."""
    # empty list
    if head is None:
        raise ValueError("Cannot call max with None")
    # base case
    if head.next is None:
        return head.value
    # recursive case
    else:
        # make a "max" variable that has a recursive call
        max_rest: int = max(head.next)
        # if the current value is greater than the next
        if head.value > max_rest:
            return head.value
        # otherwise, keep the max value
        else:
            return max_rest


def linkify(items: list[int]) -> Node | None:
    """Return a linked list of nodes."""
    # base case
    if len(items) == 0:
        return None
    # recursive case
    else:
        head: Node = Node(items[0], linkify(items[1:]))
    return head


def scale(head: Node | None, factor: int) -> Node | None:
    """Return a linked list where the values are scaled by the factor."""
    # base case
    if head is None:
        return None
    # recursive case
    else:
        # make a new variable that calls the function again
        scaled_node: Node = Node(val=head.value * factor, next=scale(head.next, factor))
        return scaled_node
