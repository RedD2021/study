n = int(input())
a = 1
b = 0
c = 1
d = 1
while n > a:
    d = b + c
    b = c
    c = d
    a += 1
print(d)
