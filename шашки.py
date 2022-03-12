x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
color1 = 1
color2 = 2
if (x1 + y1) % 2 == 0:
    color1 = 1
elif (x1 + y1) % 2 != 0:
    color1 = 2
if (x2 + y2) % 2 == 0:
    color2 = 1
elif (x2 + y2) % 2 != 0:
    color2 = 2
if color1 != color2:
    print('No')
elif y1 > y2:
    print('No')
elif y2 - y1 >= abs(x2 - x1):
    print('Yes')
