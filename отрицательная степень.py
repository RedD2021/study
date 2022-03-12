def power(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1
    i = 1
    k = a
    if n < 0:
        while i != n:
            k = k / a
            i += -1
        return k
    if n > 0:
        while i != n:
            k = k * a
            i += 1
        return k


a = float(input())
n = int(input())
print(power(a, n))
