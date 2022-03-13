def lagrange(x, pow, q):
    b = int(x ** (1 / pow))
    if x - b ** pow == 0:
        return str(b ** pow)
    if q == 1:
        return 0
    while lagrange(x - b ** pow, pow, q - 1) == 0:
        b -= 1
        if b <= 0:
            return 0
    return str(b ** pow) + ' ' + lagrange(x - b ** pow, pow, q - 1)


n = int(input())

print(lagrange(n, 3, 7))
