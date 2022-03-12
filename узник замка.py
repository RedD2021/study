a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
if a >= b:
    a, b = b, a
if b >= c:
    b, c = c, b
if a >= b:
    a, b = b, a
if d >= e:
    d, e = e, d
if b <= e and a <= d:
    print('Yes')
else:
    print('No')
