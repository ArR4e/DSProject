from math import *

while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisesta koogi mõõt: "))
    
    def koogi_hind(nimi, mõõt):
        if nimi == "šokolaadikook":
            šokolaadikoogi_hind = (pi * mõõt ** 2) * 0.06
            return round(šokolaadikoogi_hind, 2)
        elif nimi == "ploomikook":
            ploomikoogi_hind = (pi * mõõt ** 2) * 0.04
            return round(ploomikoogi_hind, 2)
        elif nimi == "Napoleoni kook":
            Napoleoni_hind = (mõõt ** 2) * 0.10
            return round(Napoleoni_hind, 2)
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud")

    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")


