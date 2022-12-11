from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = mõõt ** 2 * pi * 0.06
    elif nimi == "ploomikook":
        hind = mõõt ** 2 * pi * 0.04
    elif nimi == "Napoleoni kook":
        hind = mõõt ** 2 * 0.1
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind, 2)

while True:
    nimi = input("Sisesta koogi nimi: ").strip()
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
    if mõõt == "":
        break
    print("Koogi hind on", str(koogi_hind(nimi, mõõt)), "eurot")
