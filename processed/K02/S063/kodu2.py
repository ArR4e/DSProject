from math import *

liini_pikkus = int(input("Sisestage liini pikkus: "))
print("Elektriliini pikkus on", str(liini_pikkus)+"m")

max_kaugus = int(input("Sisestage maksimaalne postide vaheline kaugus:"))
print("Maksimaalne kaugus postide vahel on", str(max_kaugus)+"m")

postide_arv = ceil(liini_pikkus/max_kaugus)+1
print("Postide arv on", postide_arv)


