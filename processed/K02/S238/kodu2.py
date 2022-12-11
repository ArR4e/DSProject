from math import *

pikkus = int(input("sisesta liini pikkus: "))
kaugus = int(input("sisesta postide kaugus: "))

poste = ceil(pikkus / kaugus) + 1  

print(poste)