from math import *

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = round(0.06 * pi * mõõt ** 2, 2)
        return hind
    elif nimi == "ploomikook":
        hind = round(0.04 * pi * mõõt ** 2, 2)
        return hind
    elif nimi == "Napoleoni kook":
        hind = round(0.10 * mõõt ** 2, 2)
        return hind
    else:
        raise Exception ("Sellist kooki andmebaasist ei leitud")
    return hind

while True:
    nimi = str(input("Milline kook? "))
    if nimi == "":
        break
    elif nimi == "Napoleoni kook":
        mõõt = float(input("Mis on koogi külje pikkus? "))
    else:
        mõõt = float(input("Mis on koogi raadius? "))
    print("Koogi maksumus on", koogi_hind(nimi, mõõt), "€.")

