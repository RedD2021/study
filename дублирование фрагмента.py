s = input()
a = len(s) - 1
pos1 = s.find('h')
pos2 = a - s[::-1].find('h')
print(s[0:pos1] + s[pos1:pos2] + s[pos1 + 1:pos2] + s[pos2:])
