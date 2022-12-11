import math
pikkus = int(input("Sisestage liini pikkust : "))
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugust:"))
print("Teie liini ehitamiseks minimaalselt vaja: ")
print(math.ceil((pikkus/kaugus)+1))