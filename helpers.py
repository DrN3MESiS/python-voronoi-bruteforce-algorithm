import random
import math
import copy

epsilon = 1e-6


def eQF(f1, f2):
    a = f1 - f2
    if a <= epsilon:
        return True
    else:
        return False


def eQPoint(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    r1 = x1 - x2
    if r1 < 0:
        r1 = r1 * -1

    r2 = y1 - y2
    if r2 < 0:
        r2 = r2 * -1

    if r1 < epsilon and r2 < epsilon:
        return True
    else:
        return False


def rP(a, b, n):
    points = []
    for _ in range(0, n):
        points.append([random.randint(a, b), random.randint(a, b)])
    return points


def CircleIntersection(c1, c2, r):
    x1 = c1.origin[0]
    y1 = c1.origin[1]
    x2 = c2.origin[0]
    y2 = c2.origin[1]

    r1 = r
    r2 = r

    centerdx = x1 - x2
    centerdy = y1 - y2
    R = math.sqrt(centerdx * centerdx + centerdy * centerdy)

    if not ((abs(r1 - r2) <= R) and (R <= r1 + r2)):
        return []

    # intersection(s) should exist

    R2 = R * R
    R4 = R2 * R2
    a = (r1 * r1 - r2 * r2) / (2 * R2)
    r2r2 = r1 * r1 - r2 * r2
    c = math.sqrt(2 * (r1 * r1 + r2 * r2) / R2 - (r2r2 * r2r2) / R4 - 1)

    fx = (x1 + x2) / 2 + a * (x2 - x1)
    gx = c * (y2 - y1) / 2
    ix1 = fx + gx
    ix2 = fx - gx

    fy = (y1 + y2) / 2 + a * (y2 - y1)
    gy = c * (x1 - x2) / 2
    iy1 = fy + gy
    iy2 = fy - gy

    return [[int(ix1), int(iy1)], [int(ix2), int(iy2)]]
