from math import pi
def koogi_hind(nimi, moot):
    if nimi == "šokolaadikook":
        koogihind = (pi * moot**2) * 0.06
        return round(koogihind, 2)
    elif nimi == "ploomikook":
        koogihind = (pi * moot**2) * 0.04
        return round(koogihind, 2)
    elif nimi == "Napoleoni kook":
        koogihind = moot**2 * 0.1
        return round(koogihind, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

nimi = input("Sisestage koogi nimi:") 

while True:
    if nimi == "":
        break
    moot = float(input("Sisestage koogi mõõt:"))
    print("Teie koogi hind on", str(koogi_hind(nimi, moot)), ".")
    nimi = input("Sisestage koogi nimi:")




