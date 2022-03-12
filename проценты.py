p = int(input())
x = int(input())
y = int(input())
s = (x * 100) + y
ts = s + ((s * p) / 100)
print(int(ts // 100), int(ts % 100))
