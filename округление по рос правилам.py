n = float(input())
a = n * 1000000
b = a % 1000000
s = b // 100000
dig = a // 1000000
if s >= 5:
    dig += 1
print(int(dig))
