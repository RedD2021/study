a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
if a1 >= b1:
    a1, b1 = b1, a1
if b1 >= c1:
    b1, c1 = c1, b1
if a1 >= b1:
    a1, b1 = b1, a1
if a2 >= b2:
    a2, b2 = b2, a2
if b2 >= c2:
    b2, c2 = c2, b2
if a2 >= b2:
    a2, b2 = b2, a2
if c2 == c1 and b2 == b1 and a2 == a1:
    print('Boxes are equal')
elif c2 >= c1 and b2 >= b1 and a2 >= a1:
    print('The first box is smaller than the second one')
elif c2 <= c1 and b2 <= b1 and a2 <= a1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
