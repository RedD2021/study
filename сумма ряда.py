n = int(input())
a = 1
s = 0
while a <= n:
    s += 1/(a ** 2)
    a += 1
print('{0:.6f}'. format(s))
