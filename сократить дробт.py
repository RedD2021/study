def ReduceFraction(n, m):
    if n != 0 and m != 0:
        if n > m:
            return ReduceFraction(n % m, m)
        return ReduceFraction(n, m % n)
    return n + m


x = int(input())
y = int(input())
print(x // ReduceFraction(x, y), y // ReduceFraction(x, y))
