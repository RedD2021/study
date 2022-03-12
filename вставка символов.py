s = input()
a = 0
b = ''
while len(s) - 1 > a:
    b += s[a] + '*'
    a += 1
print(b + s[-1])
