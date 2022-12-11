import math
liini_pikkus = int(input("Sisestage liini pikkus: "))
max_kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
miinimum = liini_pikkus / max_kaugus
print("Liini ehitamiseks on minimaalselt vaja " + str(int(math.ceil(miinimum)) + 1) + " posti.")