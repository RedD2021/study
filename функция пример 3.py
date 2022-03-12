def max2(a, b):
    if a > b:
        return a
    return b


def max3(a, b, c):
    return max(max2(a, b), c)


print(max3(2, 5, 7))
