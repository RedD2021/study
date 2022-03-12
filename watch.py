N = int(input())
minut = N // 60
sec = N % 60
chas = minut // 60
minut2 = minut % 60
chas2 = chas % 24
print(chas2, ':', minut2 // 10, minut2 % 10, ':', sec // 10, sec % 10, sep='')
