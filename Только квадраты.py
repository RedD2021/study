import math
i = 0


def rec():
    global i
    n = int(input())
    if n != 0:
        rec()
        if n % math.sqrt(n) == 0:
            i += 1
            print(n)


rec()
if i == 0:
    print('0')
