"""examples of dictionary syntax"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len(ice_cream) = 3   --> num of key-value pairings

print(f"{len(ice_cream)} flavors")

# modify the value of the list
ice_cream["vanilla"] += 10

# remove a key from the dictionary, will return the value of the item (4 in this case)
ice_cream.pop("strawberry")

# test if a key is already in the dictionary
"pbj" in ice_cream
# <value> in <dictionary name>, will return True or False
# can even say:
has_pbj: bool = "pbj" in ice_cream

# count number of total orders
total_orders: int = 0

for flavor in ice_cream:
    # will loop through the keys, "flavor" is an unimportant name
    total_orders += ice_cream[flavor]

print(total_orders)
