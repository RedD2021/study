a = int(input())
b = int(input())
res = a % b
print('YES' * 0 ** res, 'NO' * (-1 * (0 ** res - 1)))
