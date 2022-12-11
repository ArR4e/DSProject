from math import pi


def koogi_hind(nimi, mõõt):
    if nimi == str("šokolaadikook"):
        hind = ((pi * (mõõt)**2) * 0.06)
        return round(hind, 2)
    if nimi == str("ploomikook"):
        hind = (pi * ((mõõt)**2) * 0.04)
        return round(hind, 2)
    if nimi == str("Napoleoni kook"):
        hind = ((mõõt)**2 * 0.10)
        return round(hind, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud. ")

while True:
    nimi = input("Koogi nimi: ")
    if nimi == "":
        break
    mõõt = input("Koogi mõõt: ")
    print("Koogi hind on ", koogi_hind(nimi, float(mõõt)), "eurot. ")



