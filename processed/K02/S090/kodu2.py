import math

Liini_pikkus = int(input("Palun sisestage elektriliini pikkus: "))
Postide_vahe = int(input("Palun sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
arv = (Liini_pikkus / Postide_vahe) + 1


print("Poste on vaja "+str(math.ceil(arv))+".")