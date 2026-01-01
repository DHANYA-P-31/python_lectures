from fractions import Fraction


class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff =  (self.x - other.x) ** 2
        y_diff = (self.y - other.y) ** 2
        return (x_diff + y_diff)**0.5
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Circle(object):
    def __init__(self,center,radius):
        self.center = center
        self.radius = radius

    def is_inside(self,other):
        return other.distance(self.center) < self.radius

center = Coordinate(0,0)
my_circle = Circle(center,radius=1)

point = Coordinate(0,0.5)
print(my_circle.is_inside(point))

class Fraction(object):
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def times(self, other):
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        return top / bottom

    def plus(self, other):
        top = self.numerator * other.denominator + other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        return top / bottom

    def get_inverse(self):
        return self.denominator / self.numerator

    def invert(self):
        self.denominator, self.numerator = self.numerator , self.denominator

f1 = Fraction(1,2)
f2 = Fraction(3,4)
print(f1.plus(f2))
print(f1.times(f2))
print(f1.get_inverse())
f1.invert()
print(f1.denominator, f1.numerator)
print(center)
print(f1)

class Fraction2:

    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        return Fraction2(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)

    def __mul__(self, other):
        return Fraction2(self.numerator * other.numerator, self.denominator * other.denominator)

    def __float__(self):
        return self.numerator / self.denominator

f11 = Fraction2(1,2)
f12 = Fraction2(3,4)
print(f11)
print(f12)
print(f11+f12)
print(f11*f12)
print(float(f11))