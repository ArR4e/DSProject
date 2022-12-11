#elektriliin

from math import *

#kasutajalt liini pikkus

liini_pikkus = int(input("Sisesta liini pikkus meetrites: "))

#kasutajalt postide vaheline kaugus

postide_kaugus = int(input("Sisesta postide kaugus meetrites: "))

#arvuta mitu posti on liini ehitamiseks minimaalselt vaja

postide_arv = liini_pikkus / postide_kaugus + 2

print("Minimaalselt on liini ehitamiseks poste vaja: ")

print(floor(postide_arv))


