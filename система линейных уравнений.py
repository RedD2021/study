a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
delta = a * d - b * c
delta_x = e * d - b * f
delta_y = a * f - c * e
x = delta_x / delta
y = delta_y / delta
print(x, y)
