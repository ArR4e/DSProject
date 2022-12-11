from math import ceil
liini_pikkus = float(input('Sisesta liini pikkus: '))
max_kaugus = float(input('Sisesta max kaugus: '))

print(ceil(liini_pikkus / max_kaugus) + 1)