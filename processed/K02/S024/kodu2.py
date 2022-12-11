import math

liini_pikkus = int(input("Sisestage liini pikkus meetrites: "))
max_kaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
min_postid = math.ceil((liini_pikkus / max_kaugus) + 1)
print("Liini ehitamiseks on minimaalselt vaja " + str(min_postid) + " posti.")