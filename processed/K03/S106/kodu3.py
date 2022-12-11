n = int(input('Sisesta naturaalarv: '))
arvuruudud = 0
i = 1
while i <= n:
    arvuruudud += i**2
    i += 1

print(arvuruudud)
    


summaruut = 0
i = 1
while i <= n:
    summaruut += i
    i += 1

print(summaruut ** 2)

y = summaruut ** 2 - arvuruudud
print(y)