from math import *

def koogi_hind(koogi_nimi, mõõtmed):
    if koogi_nimi == 'Napoleoni kook':
        return round((0.1*(mõõtmed**2)),2)
    elif koogi_nimi == 'šokolaadikook':
        return round((0.06*(mõõtmed**2*pi)),2)
    elif koogi_nimi == 'ploomikook':
        return round((0.04*(mõõtmed**2*pi)),2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
 
while True:
    koogi_nimi = input("Sisestage koogi nimi: ")
    if koogi_nimi == "":
        break
    else:
        mõõtmed = float(input("Sisestage koogi mõõtmed: "))
        print("Koogi hind on" , koogi_hind(koogi_nimi, mõõtmed), "eurot.")