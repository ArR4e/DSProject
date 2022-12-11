#Pagarikoda valmistab kolme sorti kooke: šokolaadikook (0,06 €/cm2), ploomikook (0,04 €/cm2) ja Napoleoni kook (0,10 €/cm2).
from math import pi
def koogi_hind(koogi_nimi, mõõt):
    if(koogi_nimi == "šokolaadikook"):
        pindala = pi * mõõt**2
        hind = 0.06 * pindala
        return round(hind, 2)
    elif (koogi_nimi == "ploomikook"):
        pindala = pi * mõõt**2
        hind = 0.04 * pindala
        return round(hind, 2)
    elif (koogi_nimi == "Napoleoni kook"):
        pindala = mõõt**2
        hind = 0.1 * pindala
        return round(hind, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")
while True:
    koogi_nimi = input("Sisestage koogi nimi (šokolaadikook,ploomikook või Napoleoni kook): ")
    if koogi_nimi == "":
        break
    mõõt = float(input("Sisestage koogi mõõt: "))
    print ("" + koogi_nimi.title() + "", "koogi hind on", koogi_hind(koogi_nimi, mõõt), "eurot.")