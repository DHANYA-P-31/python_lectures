## Creating and using classes in python

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff =  (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        return (x_diff + y_diff)**0.5

c = Coordinate(4,3)
origin = Coordinate(0,0)

print(c.x, c.y)
print(origin.x, origin.y)

print(c.distance(origin))