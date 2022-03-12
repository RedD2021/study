s = input()
pos1 = s.find('h')
pos2 = s.rfind('h')
a = s[pos1 + 1:pos2]
print(s[:pos1 + 1] + a.replace('h', 'H') + s[pos2:])
