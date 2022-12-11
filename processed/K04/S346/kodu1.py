from math import pi
def koogi_hind(nimi, mõõt):
    if (nimi == "Napoleoni kook"):
        pindala = mõõt**2
        hind = 0.10 * pindala
        return round(hind, 2)
    elif (nimi == "šokolaadikook"):
        pindala = pi * mõõt**2
        hind = 0.06 * pindala
        return round(hind, 2)
    elif (nimi == "ploomikook"):
        pindala = pi * mõõt**2
        hind = 0.04 * pindala
        return round(hind, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
while True:
    nimi = input("Palun sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Palun sisestage koogi mõõt: "))
    print("Koogi hind on ", koogi_hind(nimi, mõõt), "eurot.")
    