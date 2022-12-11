from math import *

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        #Arvutab hinna
        hind = pi * mõõt * mõõt * 0.06
    elif nimi == "ploomikook":
        #Arvutab hinna
        hind = pi * mõõt * mõõt * 0.04
    elif nimi == "Napoleoni kook":
        #Arvutab hinna
        hind = mõõt * mõõt * 0.10
    else: 
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind, 2)

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    #Kui kooginimi on tühi siis lõpetab
    if koogi_nimi == "":
        break
    try:
        koogi_mõõt = float(input("Sisesta koogi mõõt: "))
    except:
        #Kui koogimõõt pole number
        print("Koogimõõt peab olema numbrites")
        continue
    print(f"{koogi_nimi} maksab {koogi_hind(koogi_nimi, koogi_mõõt)} eurot.")