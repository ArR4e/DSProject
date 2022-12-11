from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = (pi * mõõt ** 2) * 0.06
        return round(hind, 2)
    elif nimi == "ploomikook":
        hind = (pi * mõõt ** 2) * 0.04
        return round(hind, 2)
    elif nimi == "Napoleoni kook":
        hind = (mõõt **2) * 0.1
        return round(hind, 2)
    else: 
        raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
         break
    mõõt = float(input("Sisesta koogi raadius või küljepikkus cm-s: "))
    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")
