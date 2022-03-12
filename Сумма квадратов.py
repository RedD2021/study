n = int(input())
a = 1
kv = 0
sumKv = 0
while a <= n:
    kv = a ** 2
    sumKv += kv
    a += 1
print(sumKv)
