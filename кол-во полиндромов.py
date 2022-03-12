n = int(input())
a = 1
count = 0
while a <= n:
    i = 0
    dig = 0
    dig1 = 0
    while (a // 10 ** i) != 0:
        dig = (a // 10 ** i) % 10
        dig1 = dig1 * 10 + dig
        i += 1
    if dig1 == a:
        count += 1
    a += 1
print(count)
