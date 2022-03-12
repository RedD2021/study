def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


a, b = float(input()), float(input())
if IsPointInSquare(a, b):
    print("YES")
else:
    print("NO")
