l1, w1, h1 = int(input()), int(input()), int(input())
l2, w2, h2 = int(input()), int(input()), int(input())
lc, wc, hc = int(input()), int(input()), int(input())
if h1 > hc or h2 > hc:
    print('NO')
elif lc < l1 > wc or lc < w1 > wc:
    print('NO')
elif lc < l2 > wc or lc < w2 > wc:
    print('NO')
elif h1 + h2 <= hc:
    print('Yes')
elif l1 + l2 <= lc and w1 <= wc >= w2:
    print('Yes')
elif l1 + w2 <= lc and w1 <= wc >= l2:
    print('Yes')
elif l1 + l2 <= wc and w1 <= lc >= w2:
    print('Yes')
elif l1 + w2 <= wc and w1 <= lc >= l2:
    print('Yes')
elif l1 <= lc >= l2 and w1 + w2 <= wc:
    print('Yes')
elif l1 <= lc >= w2 and w1 + l2 <= wc:
    print('Yes')
elif l1 <= wc >= l2 and w1 + w2 <= lc:
    print('Yes')
elif l1 <= wc >= w2 and w1 + l2 <= lc:
    print('Yes')
else:
    print('No')
