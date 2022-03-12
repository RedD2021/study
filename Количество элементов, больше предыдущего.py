n1 = int(input())
a = 0
while n1 != 0:
    n2 = int(input())
    if n2 > n1:
        a += 1
    n1 = n2
print(a)
