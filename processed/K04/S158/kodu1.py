from math import *

def koogi_hind(koogi_nimi, koogi_mõõt) :
    if koogi_nimi == "Napoleoni kook":
        return round(0.1 * koogi_mõõt**2, 2)
    elif koogi_nimi == "šokolaadikook":
        return round(0.06 * pi * koogi_mõõt**2, 2)
    elif koogi_nimi == "ploomikook":
        return round(0.04 * pi * koogi_mõõt**2, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud!")

while True:
    koogi_nimi = str(input("Sisesta koogi tüüp: "))
    if koogi_nimi == "":
        break
    else:
        koogi_mõõt = float(input("Sisestage koogi küljepikkus/raadius sentimeetrites: "))
        print("Koogi hind on ", str(koogi_hind(koogi_nimi, koogi_mõõt)), " eurot.")       



