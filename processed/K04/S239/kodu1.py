from math import *

def koogi_hind(nimi,mõõt):
    if nimi.lower()=="šokolaadikook":
        hind=0.06*pi*mõõt**2
        print("Koogi hind on ",str(round(hind,2))," €")
        return round(hind,2)
    elif nimi.lower()=="ploomikook":
        hind=0.04*pi*mõõt**2
        print("Koogi hind on ",str(round(hind,2))," €")
        return round(hind,2)
    elif nimi.lower()=="napoleoni kook":
        hind=0.1*mõõt**2
        print("Koogi hind on ", str(round(hind,2))," €")
        return round(hind,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi=input("Millist kooki Te soovite? ")
    if nimi=="":
        break
    mõõt=float(input("Kui suurt kooki Te soovite? "))
    koogi_hind(nimi,mõõt)