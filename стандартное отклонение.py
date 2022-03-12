import math

n = int(input())
i = 0
s = n
sq = n ** 2
while n != 0:
    n = int(input())
    i += 1
    s += n
    sq += n ** 2
s = math.sqrt((sq - ((s ** 2) / i)) / (i - 1))
print(s)
