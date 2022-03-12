now = int(input())
sumSeq = now
a = 0
while now != 0:
    a += 1
    now = int(input())
    sumSeq += now
print(sumSeq / a)
