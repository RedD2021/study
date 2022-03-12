a, b = int(input()), int(input())
c, d = int(input()), int(input())
e, f = int(input()), int(input())
r1 = b - a
r2 = d - c
r3 = f - e
if (a <= d and c <= b) and (c <= f and e <= d):
    print(0)
elif (a <= f and e <= b) and (c <= f and e <= d):
    print(0)
elif (a <= f and e <= b) and (a <= d and c <= b):
    print(0)
elif c <= f and e <= d:
    print(1)
elif d < e <= d + r1:
    print(1)
elif f < c <= f + r1:
    print(1)
elif a <= f and e <= b:
    print(2)
elif b < e <= b + r2:
    print(2)
elif f < a <= f + r2:
    print(2)
elif a <= d and c <= b:
    print(3)
elif b < c <= b + r3:
    print(3)
elif d < a <= d + r3:
    print(3)
else:
    print(-1)
