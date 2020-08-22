# -*- coding: utf-8 -*-
class Vector(object):
    CELL_SIZE = (24, 24)

    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = 0
            self.y = 0

    def get(self):
        # type: () -> tuple
        """return tuple of vector"""
        return (self.x, self.y)

    def to_abs(self):
        # type: () -> Vector
        """return absolute vector of cell"""
        return self * Vector(Vector.CELL_SIZE)

    def to_rel(self):
        # type: () -> Vector
        """return relative vector of cell"""
        return self // Vector(Vector.CELL_SIZE)

    def cell_center(self):
        # type: () -> Vector
        """return absolute vector of cell center"""
        return (self.to_rel() + Vector(.5, .5)).to_abs()

    def floor(self):
        # type: () -> Vector
        """return vector with integer coordinates"""
        return Vector(int(self.x), int(self.y))

    def get_square_length(self):
        # type: () -> float
        return (self.x ** 2 + self.y ** 2)

    def get_length(self):
        # type: () -> float
        """return length of vector"""
        return self.get_square_length() ** 0.5

    def __lt__(self, other):
        if other.__class__ == self.__class__:
            return self.get_square_length() < other.get_square_length()
        else:
            raise TypeError("unsupported operand type(s) for <: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __gt__(self, other):
        if other.__class__ == self.__class__:
            return self.get_square_length() > other.get_square_length()
        else:
            raise TypeError("unsupported operand type(s) for >: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __le__(self, other):
        if other.__class__ == self.__class__:
            return not (self > other)
        else:
            raise TypeError("unsupported operand type(s) for <=: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __ge__(self, other):
        if other.__class__ == self.__class__:
            return not (self < other)
        else:
            raise TypeError("unsupported operand type(s) for >=: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __eq__(self, other):
        if other.__class__ == self.__class__:
            return (self.x == other.x) and (self.y == other.y)
        else:
            return False

    def __ne__(self, other):
        if other.__class__ == self.__class__:
            return not self.__eq__(other)

    def __add__(self, other):
        if other.__class__ == self.__class__:
            return Vector(self.x + other.x, self.y + other.y)
        elif other.__class__ == tuple:
            return Vector(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("unsupported operand type(s) for +: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __sub__(self, other):
        if other.__class__ == self.__class__:
            return Vector(self.x - other.x, self.y - other.x)
        elif other.__class__ == tuple:
            return Vector(self.x - other[0], self.y - other[1])
        else:
            raise TypeError("unsupported operand type(s) for -: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __mul__(self, other):
        if other.__class__ in [int, float]:
            return Vector(self.x * other, self.y * other)
        elif other.__class__ == self.__class__:
            return Vector(self.x * other.x, self.y * other.y)
        elif other.__class__ == tuple:
            return Vector(self.x * other[0], self.y * other[1])
        else:
            raise TypeError("unsupported operand type(s) for *: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if other.__class__ in [int, float]:
            return Vector(self.x / other, self.y / other)
        elif other.__class__ == self.__class__:
            return Vector(self.x / other.x, self.y / other.y)
        elif other.__class__ == tuple:
            return Vector(self.x / other[0], self.y / other[1])
        else:
            raise TypeError("unsupported operand type(s) for /: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __floordiv__(self, other):

        if other.__class__ in [int, float]:
            return Vector(int(self.x // other), int(self.y // other))
        elif other.__class__ == tuple:
            return Vector(int(self.x // other[0]), int(self.y // other[1]))
        elif other.__class__ == self.__class__:
            return Vector(int(self.x // other.x), int(self.y // other.y))
        else:
            raise TypeError("unsupported operand type(s) for //: '{first}' "
                            "and '{second}'".format(
                first=self.__class__.__name__,
                second=other.__class__.__name__))

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


class Direction(Vector):
    UP = Vector(0, -1)
    DOWN = Vector(0, 1)
    RIGHT = Vector(1, 0)
    LEFT = Vector(-1, 0)
    ZERO = Vector(0, 0)
    ALL = (UP, LEFT, DOWN, RIGHT)
