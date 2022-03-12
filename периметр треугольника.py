from math import sqrt


def distance(x1, y1, x2, y2):
    result = sqrt((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2))
    return result


a1, b1, a2, b2 = float(input()), float(input()), float(input()), float(input())
a3, b3 = float(input()), float(input())
ab = distance(a1, b1, a2, b2)
bc = distance(a2, b2, a3, b3)
ac = distance(a1, b1, a3, b3)
perimetr = ab + bc + ac
print('{0:.10f}'.format(perimetr))
