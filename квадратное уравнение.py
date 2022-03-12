import math

a = float(input())
b = float(input())
c = float(input())
x, x1, x2 = 0, 0, 0
D = (b ** 2) - (4 * a * c)
if D < 0:
    print('')
elif D > 0:
    x1 = ((-1 * b) + math.sqrt(D)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(D)) / (2 * a)
    if x1 > x2:
        print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
    else:
        print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
elif D == 0:
    x = ((-1 * b) / (2 * a))
    print('{0:.6f}'. format(x))
