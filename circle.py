import math


class Circle:
    isCurrentlyIntersecting = False
    name = ""
    origin = (0, 0)

    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def __repr__(self):
        return f"< {self.name} C: {self.origin}>"

    def PointIsInside(self, x, y, r):
        x0 = self.origin[0]
        y0 = self.origin[1]
        dx = ABS(x - x0)
        dy = ABS(y - y0)
        return math.sqrt(dx * dx + dy * dy) < r


def ABS(x):
    if x < 0:
        return 0 - x
    else:
        return x
