n = int(input())
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
res = ((a * 10 + b) - (d * 10 + c)) + 1
print(res)
