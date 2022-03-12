n = int(input())
i = int(input())
while n != i:
    if n % 2 == 0 and n // 2 >= i:
        n = n // 2
        print(':2')
    elif n % 2 == 0 and n // 2 < i:
        n -= 1
        print(-1)
    elif n % 2 != 0:
        n -= 1
        print(-1)
