from math import *

def koogi_hind(x,y):
    if kook == "šokolaadikook":
        koogi_hind = pi * mõõt**2 * 0.06
        return(round(koogi_hind, 2))
    elif kook == "ploomikook":
        koogi_hind = pi * mõõt**2 * 0.04
        return(round(koogi_hind, 2))
    elif kook == "Napoleoni kook":
        koogi_hind = mõõt**2 * 0.1
        return(round(koogi_hind, 2))
    else:
        raise Exception("Sellist kooki anmdebaasist ei leitud")

while True:
    kook = str(input("Sisestage koogi nimi: "))
    if kook == "":
        break
    else:
        mõõt = float(input("Sisestage koogi mõõt: "))
        print(koogi_hind(kook, mõõt))