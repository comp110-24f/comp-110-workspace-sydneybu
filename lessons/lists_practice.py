# creating a list variable that is initially empty
my_numbers: list[float] = []  # literal version
print(my_numbers)  # should print []

# this does the exact same thing -> my_numbers: list[float] = list () #constructor version

# add (aka append) a value
my_numbers.append(1.5)
print(my_numbers)  # should print [1.5]

# make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points)  # should print [102, 86, 94]

# print 94 in our list
print(game_points[2])
# OR
print(game_points[len(game_points) - 1])

# modifying by index (change 86 to 72)
game_points[1] = 72

# can we change individual characters in a string?
my_name: str = "Izzi"
# my_name[3] = "y"
# does not work!!

# convert the string to a list
name_as_list: list[str] = list(my_name)
print(name_as_list)  # should return ["I, "z", "z", "i"]
name_as_list[3] = "y"  # should return ["I, "z", "z", "y"]

# remove 72 from game_points
game_points.pop(1)
print(game_points)  # should return [102, 94]

game_points.append(102)
print(game_points)
