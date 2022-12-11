from math import *

liin = int(input("Sisesta liini pikkus meetrites: "))
kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
if liin<kaugus or liin==kaugus:
    print("Minimaalselt on vaja", 2, "posti.")
elif liin%kaugus==0:
    print("Minimaalselt on vaja", liin//kaugus + 1, "posti.")
else:
    print("Minimaalselt on vaja", liin//kaugus + 2, "posti.")