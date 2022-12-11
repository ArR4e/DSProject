from math import pi

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        koogi_hind = pi * koogi_mõõt ** 2 * 0.06
        koogi_hind = round(koogi_hind, 2)
        print("Koogi hind on", koogi_hind, "eurot")
        return koogi_hind
    elif koogi_nimi == "ploomikook":
        koogi_hind = pi * koogi_mõõt ** 2 * 0.04
        koogi_hind = round(koogi_hind, 2)
        print("Koogi hind on", koogi_hind, "eurot")
        return koogi_hind
    elif koogi_nimi == "Napoleoni kook":
        koogi_hind = koogi_mõõt ** 2 * 0.1
        koogi_hind = round(koogi_hind, 2)
        print("Koogi hind on", koogi_hind, "eurot")
        return koogi_hind
    else:
        print("Sellist kooki andmebaasist ei leitud")


while True:
    koogi_nimi = input("Sisesta koogi nimi")
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Sisesta koogi mõõt"))
    koogi_hind(koogi_nimi, koogi_mõõt)
