s = input()
a = len(s)
pos1 = s.find('h')
pos2 = a - s[::-1].find('h')
print(s[0:pos1] + s[pos2:])
