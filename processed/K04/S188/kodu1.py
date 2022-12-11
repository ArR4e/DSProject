from math import *

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        return round((pi * float(koogi_mõõt) ** 2) * 0.06, 2)
    elif koogi_nimi == "ploomikook":
        return round((pi * float(koogi_mõõt) ** 2) * 0.04, 2)
    elif koogi_nimi == "Napoleoni kook":
        return round(float(koogi_mõõt) ** 2 * 0.10, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_mõõt = input("Sisesta koogi mõõt sentimeetrites: ")
    print("Sellise koogi hind on " + str(koogi_hind(koogi_nimi, koogi_mõõt)) + " eurot.")
