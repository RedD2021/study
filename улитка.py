h = int(input())
a = int(input())
b = int(input())
speed = a - b
maxh = h - a
day = ((maxh + speed - 1) // speed) + 1
print(day)
