num = int(input())
a = 1
kvadrat = a ** 2
while kvadrat <= num:
    print(a ** 2, end=' ')
    a = a + 1
    kvadrat = a ** 2
