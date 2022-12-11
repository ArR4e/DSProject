from math import *

liini_pikkus = float(input("Sisesta liini pikkus: "))
postide_vahe = float(input("Sisesta postide vaheline kaugus: "))
poste = liini_pikkus/postide_vahe
if poste <= 1:
    print (2)
else:
    if poste <= 2:
        print(3)
    else:
        print (ceil(poste))