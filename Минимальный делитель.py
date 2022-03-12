def MinDivisor(n):
    k = 2
    while n ** 0.5 >= k:
        if n % k == 0:
            return k
        else:
            k += 1
    return n


a = int(input())
print(MinDivisor(a))
