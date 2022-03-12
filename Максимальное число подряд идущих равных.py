n = int(input())
a = n
b = 1
c = 1
while n != 0:
    n = int(input())
    if n == a:
        b += 1
        if b > c:
            c = b
    elif n != a:
        b = 1
        a = n
print(c)
