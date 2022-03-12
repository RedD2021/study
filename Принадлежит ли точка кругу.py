import math


def IsPointInCircle(x, y, xc, yc, r):
    return math.sqrt((xc - x)**2 + (yc-y)**2) <= r


a, b = float(input()), float(input())
ac, bc, rad = float(input()), float(input()), float(input())
if IsPointInCircle(a, b, ac, bc, rad):
    print("YES")
else:
    print("NO")
