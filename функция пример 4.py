def sort2 (a, b):
    if a > b:
        return b, a
    return a, b


minimum, maximum = sort2(5, 4)
print(minimum, maximum)
