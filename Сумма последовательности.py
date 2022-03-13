def summa():
    n = int(input())
    if n != 0:
        n = n + summa()
    return n


print(summa())
