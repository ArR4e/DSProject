from math import *

liini_pikkus = int(input("Sisestage elektriliini pikkus meetrites: "))
postide_vahemaa = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
print("Liini ehitamiseks on minimaalselt vaja " + str(ceil(liini_pikkus/postide_vahemaa) + 1) + " posti.")