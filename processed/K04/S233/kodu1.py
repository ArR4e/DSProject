from math import *

def koogi_hind(nimi,mõõt):
    
    if nimi == "šokolaadikook":
        pindala = pi*(mõõt**2)
        return((round(pindala * 0.06,2)))
    elif nimi == "ploomikook":
        pindala = pi*(mõõt**2)
        return(round(pindala * 0.04,2))
    elif nimi == "Napoleoni kook":
        pindala = mõõt**2
        return(round(pindala * 0.10,2))
    else:
        raise Exception("Sellist kooki ei leitud")

while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisestage koogi mõõt: "))
    
    print(koogi_hind(nimi,mõõt))
