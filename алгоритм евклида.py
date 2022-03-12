def gcd(a, b):
    if a != 0 and b != 0:
        if a > b:
            return gcd(a % b, b)
        return gcd(a, b % a)
    return a + b


x = int(input())
y = int(input())
print(gcd(x, y))
