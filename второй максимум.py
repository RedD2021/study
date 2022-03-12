n = int(input())
a = n
b = 0
while n != 0:
    n = int(input())
    if n >= a:
        b = a
        a = n
    elif b < n < a:
        b = n
print(b)
