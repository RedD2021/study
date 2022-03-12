i = int(input())
maks = i
while i != 0:
    i = int(input())
    if i != 0 and maks < i:
        maks = i
print(maks)
