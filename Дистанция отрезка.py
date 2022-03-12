from math import sqrt


def distance(x1, y1, x2, y2):
    result = sqrt((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2))
    return result


a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input())
print('{0:.5f}'.format(distance(a1, b1, a2, b2)))
