from CQs.cq09.point import Point

"""check methods for correctness"""

__author__ = "730753182"

# make a Point
point = Point(1.0, 2.0)

# mutate the point
point.scale_by(2)

# check it was mutated
print(point.x)
print(point.y)

# make a new point
new_point = point.scale(3)

# print the new point
print(new_point.x)
print(new_point.y)

# check the original point was not mutated
print(point.x)
print(point.y)
