s = input()
a = len(s) - 1
if s.find('f') > -1:
    if s.find('f') == a - s[::-1].find('f'):
        print(s.find('f'))
    else:
        print(s.find('f'), a - s[::-1].find('f'))
