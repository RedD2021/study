A = int(input())
if A % 400 == 0:
    print('Yes')
else:
    if A % 100 != 0 and A % 4 == 0:
        print('Yes')
    else:
        print('No')
