k, m, n = int(input()), int(input()), int(input())
a = n * 2
if n <= k:
    print(m * 2)
elif a % k == 0:
    print(a // k * m)
elif a % k != 0:
    print(a // k * m + m)
