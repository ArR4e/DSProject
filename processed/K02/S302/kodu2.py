from math import *
pikkus = int(input("Sisestage liini pikkus: "))
maks = int(input("Sisestage kõrvutiasetsevate postide maksimaalkaugus: "))

postid = ceil(pikkus / maks) + 1
print("Liini ehitamiseks on vaja " + str(postid) + " posti.")