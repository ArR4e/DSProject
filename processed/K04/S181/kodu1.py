import math


def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = mõõt**2 * math.pi * 0.06
    elif nimi == "ploomikook":
        hind = mõõt**2 * math.pi * 0.04
    elif nimi == "Napoleoni kook":
        hind = mõõt**2 * 0.1
    elif nimi == "":
        return
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return print(round(hind,2))
       

while True:
    kook = input("Sisestage koogi nimi: ")
    suurus = float(input("Sisestage koogi mõõt: "))
    koogi_hind(kook, suurus)
