import math

a = float(input())
b = float(input())
c = float(input())
x = 1
d = b ** 2 - 4 * a * c
if d < 0:
    print(0)
elif a == 0 and b == 0 and c == 0:
    print(3)
elif a == 0 and b != 0 and c != 0:
    print(1, '{0:.6f}'.format(-c / b))
elif a == 0 and b == 0 and c != 0:
    print(0)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    if x1 > x2:
        print(2, '{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
    else:
        print(2, '{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
elif d == 0:
    print(1, '{0:.6f}'.format(-b / (2 * a)))
