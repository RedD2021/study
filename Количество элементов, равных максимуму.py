n = int(input())
a = 1
b = 0
while n != 0:
    if n == a:
        b += 1
    elif n > a:
        a = n
        b = 1
    n = int(input())
print(b)
