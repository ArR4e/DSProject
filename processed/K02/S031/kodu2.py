from math import ceil
pikkus = int(input('Sisesta liini pikkus: '))
maksimum = int(input('Sisesta maksimaalne postidevaheline kaugus: '))
print(ceil(pikkus/maksimum)+1)