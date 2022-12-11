# 1. Pagarikoja kassaaparaat / RP
from math import *

def koogi_hind(nimi, mõõt):
    while True:
        if nimi == "šokolaadikook":
            return round(0.06 * (pi * (mõõt ** 2)), 2)
        elif nimi == "ploomikook":
            return round(0.04 * (pi * (mõõt ** 2)), 2)
        elif nimi == "Napoleoni kook":
            return round(0.1 * (mõõt ** 2), 2)
        elif nimi == "":
            break
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud.")
        continue

while True:
    kook = input("Sisesta koogi nimi: ")
    if kook == "":
        break
    pikkus = float(input("Sisesta koogi pikkus: "))
    if koogi_hind(kook, pikkus) == None:
        break
    print(koogi_hind(kook, pikkus))