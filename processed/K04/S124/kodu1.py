#šokolaadikook (0,06 €/cm2) ring
#ploomikook (0,04 €/cm2) ring
#Napoleoni kook (0,10 €/cm2) ruut
from math import *

def koogi_hind(nimi, mõõt):

    if nimi == "šokolaadikook":
        pindala = pi * mõõt ** 2
        hind = pindala * 0.06
        
    elif nimi == "ploomikook":
        pindala = pi * mõõt ** 2
        hind = pindala * 0.04
        
    elif nimi == "Napoleoni kook":
        pindala = mõõt ** 2
        hind = pindala * 0.1
        
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
    
    return round(hind, 2)

while True:
    nimi = input("Sisesta soovitav kook - 'šokolaadikook', 'plooomikook' või 'Napoleoni kook': ")

    if nimi == (""):
        break
    
    mõõt = float(input("Sisesta mõõt: "))
        
    hind = koogi_hind(nimi, mõõt)
    print("Koogi hind on", hind, "eurot.")



