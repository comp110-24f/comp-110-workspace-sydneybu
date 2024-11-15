"""practice with recursive structures"""

from __future__ import annotations

# lets us refer to Node from the Node class definition


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    # magic method!! double underscore = automatic funtion call
    def __str__(self) -> str:
        rest: str = ""
        if self.next is None:  # base case
            rest = "None"
        else:
            rest = str(self.next)  # calls the function again w the next node
        return f"{self.value} -> {rest}"

        # print("wow!")


two: Node = Node(2, None)
one: Node = Node(1, two)

# print(one)
# results in <__main__.Node object at 0x10063.....
# the location of where this object is stored in memory
# print(one)
# now with the magic method __str__, this prints "wow!"
print(one)
# one is NOT the last node in the linked list
# so the function is called again on two, which is the end of the list
# would return 1 -> 2 -> None


def last(head: Node) -> int | None:
    if head.next is None:  # base case
        return head.value
    else:
        print(last(head.next))
        # stack overflow error if this was last(head)-- stuck in a recursive loop


def value_at(head: Node | None, index: int) -> int:
    """Return the data of the Node at the given index."""
    # base case of empty list
    if head is None:
        raise IndexError("Index is out of bounds on the list.")

    # base case of correct index
    if index == 0:
        return head.value

    # move to the next node
    return value_at(head.next, index -= 1)

def recursive_range(start: int, end: int) -> Node | None:
    """creates a linked list w/ values from start to end"""
    # edge case
    if start > end:
        raise ValueError("Start cannot be greater than end.")
    # base case
    if start == end:
        return None
    # recursive case -- call function again
    else:
        first: int = start
        rest: Node | None = recursive_range(start+1, end)
        return Node(first, rest)
    
    ## by printing any call to this function, the magic method __str__ is called
    ## and transforms the output from (1, Node (2, Node))..etc to 1 -> 2 -> ... None

print(recursive_range(1, 21))