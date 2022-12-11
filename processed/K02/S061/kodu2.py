from math import *
liini_pikkus = int(input("Sisesta liini pikkus: "))
max_kaugus = int(input("Sisesta maks. kaugus: "))

min_posti = ceil(liini_pikkus / max_kaugus) + 1

if max_kaugus == liini_pikkus:
    min_post = 2
elif max_kaugus > liini_pikkus:
    min_post = 2

print(min_posti)