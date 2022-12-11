from math import ceil
liini_pikkus = int(input("Sisestage liini pikkus: "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
poste = liini_pikkus / maksimaalkaugus + 1

print("Poste on kokku ", (ceil(poste)))
