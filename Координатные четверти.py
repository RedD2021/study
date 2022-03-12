x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
chapter1 = 1
chapter2 = 1
if x1 > 0 < y1:
    chapter1 = 1
elif x1 < 0 < y1:
    chapter1 = 2
elif x1 < 0 > y1:
    chapter1 = 3
elif x1 > 0 > y1:
    chapter1 = 4
if x2 > 0 < y2:
    chapter2 = 1
elif x2 < 0 < y2:
    chapter2 = 2
elif x2 < 0 > y2:
    chapter2 = 3
elif x2 > 0 > y2:
    chapter2 = 4
if chapter1 == chapter2:
    print('Yes')
else:
    print('No')
