n = int(input())
a = 1
b = 0
c = 1
e = 1
while e < n:
    e = b + c
    b, c = c, e
    a += 1
if n == 0:
    print(0)
elif n != e:
    print(-1)
else:
    print(a)
