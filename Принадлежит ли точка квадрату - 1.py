def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


a, b = float(input()), float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
