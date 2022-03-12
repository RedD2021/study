s = input()
pos = s.find('f')
posF = 0
i = 1
if pos == -1:
    print(-2)
while pos != -1:
    i += 1
    pos = s.find('f', pos + 1)
    if i == 2:
        posF = pos
        print(posF)
if i == 1 and pos != -1:
    print(-1)
