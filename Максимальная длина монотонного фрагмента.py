n1, n, c1, c2, c3, c4 = int(input()), int(input()), 1, 1, 1, 1
while n != 0:
    if n > n1:
        c1 += 1
        c3 = 1
        if c1 > c2:
            c2 = c1
    elif n < n1:
        c3 += 1
        c1 = 1
        if c3 > c4:
            c4 = c3
    elif n == n1:
        c1 = 1
        c3 = 1
    n1 = n
    n = int(input())
print(max(c2, c4))
