def phib(n):
    if n <= 2:
        return 1
    return phib(n - 1) + phib(n - 2)


a = int(input())
print(phib(a))
