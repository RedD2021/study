num = int(input())
i = 1
while i < num:
    i = i * 2
if num % i == 0:
    print('YES')
else:
    print('NO')
