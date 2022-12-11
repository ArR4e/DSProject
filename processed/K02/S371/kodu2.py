from math import *

liini_pikkus = int(input("Sisestage liini pikkus meetrites (täisarv): "))
maksimaalkaugus = int(input("Sisestage kõrvutiasetsevate postidemaksimaalkaugus meetrites (täisarv): "))

postide_arv = liini_pikkus / maksimaalkaugus + 1

print("Liini ehitamiseks läheb minimaalsel vaja", ceil(postide_arv), "posti.")