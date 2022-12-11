from math import *

pikkus = int(input("Liini pikkus: "))
maxvahe = int(input("Maksimaalne vahe: "))
if pikkus%maxvahe == 0:
    print((pikkus/maxvahe)+1)
else:
    print(ceil((pikkus/maxvahe))+1)
