def xor(x, y):
    return (x == 0 and y == 1 or
            x == 1 and y == 0)


a, b = int(input()), int(input())
if xor(a, b):
    print("1")
else:
    print("0")
