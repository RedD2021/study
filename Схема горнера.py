n = int(input())
x = float(input())
a = float(input())
i = 1
p = a
while i <= n:
    a = float(input())
    p = p * x + a
    i += 1
print('{0:.2f}'.format(p))
