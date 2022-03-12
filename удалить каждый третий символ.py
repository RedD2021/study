s = input()
a = 0
b = ''
while len(s) - 1 >= a:
    if a % 3 == 0:
        a += 1
    else:
        b += s[a]
        a += 1
print(b)
