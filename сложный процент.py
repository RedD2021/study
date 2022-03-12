p = int(input())
x = int(input())
y = int(input())
k = int(input())
a = 1
while a <= k:
    s = (x * 100) + y
    ts = s + int((s * p) / 100)
    x = ts // 100
    y = ts % 100
    a += 1
print(int(x), int(y))
