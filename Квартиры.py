x = int(input())
y = int(input())
a = x - 1
b = y - a
if x == 1:
    print('Yes')
elif a % b == 0:
    print('Yes')
else:
    print('No')
