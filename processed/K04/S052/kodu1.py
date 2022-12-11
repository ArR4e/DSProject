import math

nimi = input("Sisesta koogi nimi: ")
mõõt = float(input("Sisesta koogimõõt: "))

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook" and mõõt > 0:
        hind = 0.06 * math.pi * mõõt**2
        print(round(hind,2))
    elif nimi == "ploomikook" and mõõt > 0:
        hind = 0.04 * math.pi * mõõt**2
        print(round(hind,2))
    elif nimi == "Napoleoni kook" and mõõt > 0:
        hind = mõõt**2 * 0.1
        print(round(hind,2))
    else:
        print("Sellist kooki andmebaasist ei leitud või sisestatud mõõt on negatiivne.")

koogi_hind(nimi, mõõt)
