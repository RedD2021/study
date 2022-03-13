def C(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if n == 0:
        return 0
    return C(n - 1, k) + C(n - 1, k - 1)


a = int(input())
b = int(input())
print(C(a, b))
