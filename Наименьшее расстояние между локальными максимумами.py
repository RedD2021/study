n0 = int(input())
n1 = int(input())
n2 = int(input())
iMin = 0
locMax = 0
i = 1
while n2 != 0:
    if n0 < n1 > n2:
        locMax += 1
        if locMax == 2:
            iMin = i
            i = 1
        elif locMax > 2 and iMin > i:
            iMin = i
            i = 1
        else:
            i = 1
    else:
        i += 1
    n0 = n1
    n1 = n2
    n2 = int(input())
print(iMin)
