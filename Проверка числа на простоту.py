def IsPrime(n):
    k = 2
    while n ** 0.5 >= k:
        if n % k == 0:
            return print('NO')
        else:
            k += 1
    return print('YES')


a = int(input())
IsPrime(a)
