n = int(input())
a, b, c = 0, 0, n
while c != 0:
    c //= 10
    a += 1
while b < a:
    c += 10**(a - b - 1) * ((n // 10**b) % 10)
    b += 1
print(c)
