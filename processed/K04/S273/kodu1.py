from math import *

def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        return (round((pi*mõõt**2)*0.06, 2))
    if nimi == "ploomikook":
        return (round((pi*mõõt**2)*0.04, 2))
    if nimi == "Napoleoni kook":
        return (round((mõõt**2)*0.10, 2))
    else:
        print("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input("Mis on koogi nimi? ")
    if nimi == "":
        break
    mõõt = float(input("Mis on koogi mõõt? "))
    hind = koogi_hind(nimi,mõõt)
    print("Koogi hind on", hind, "eurot.")