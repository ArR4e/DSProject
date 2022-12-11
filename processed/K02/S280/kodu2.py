# RP / 2. Elektriliin
from math import *

liinipikkus = int(input("Sisestage liini pikkus (m): "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus (m): "))

postid = 1 + ceil(liinipikkus / maksimaalkaugus)
print("Poste läheb minimaalselt vaja: " + str(postid))