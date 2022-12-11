from math import*
pikkus = int(input("Sisestage liini pikkus: "))
kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))
postidearv = ceil(pikkus / kaugus) + 1
print("Liini ehitamiseks on minimaalselt vaja " + str(postidearv) + " posti.")
    
