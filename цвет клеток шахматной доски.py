x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
color1 = 1
color2 = 2
if x1 % 2 == 1 and y1 % 2 == 1 or x1 == y1:
    color1 = 1
elif x1 % 2 == 0 and y1 % 2 == 0:
    color1 = 1
elif x1 % 2 == 1 and y1 % 2 == 0:
    color1 = 2
elif x1 % 2 == 0 and y1 % 2 == 1:
    color1 = 2
if x2 % 2 == 1 and y2 % 2 == 1 or x2 == y2:
    color2 = 1
elif x2 % 2 == 0 and y2 % 2 == 0:
    color2 = 1
elif x2 % 2 == 1 and y2 % 2 == 0:
    color2 = 2
elif x2 % 2 == 0 and y2 % 2 == 1:
    color2 = 2
if color1 == color2:
    print('Yes')
else:
    print('No')
