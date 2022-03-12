x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if ((x2 == x1 + 1) or (x2 == x1 - 1) or (x2 == x1)) and (x2 >= 1):
    if ((y2 == y1 + 1) or (y2 == y1 - 1) or (y2 == y1)) and (y2 >= 1):
        print('Yes')
    else:
        print('No')
else:
    print('No')
