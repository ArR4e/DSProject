import math

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        return round(math.pi * koogi_mõõt**2 * 0.06, 2)
    elif koogi_nimi == "ploomikook":
        return round(math.pi * koogi_mõõt**2 * 0.04, 2)
    elif koogi_nimi == "Napoleoni kook":
        return round(koogi_mõõt**2 * 0.1, 2)
    raise Exception("Sellist kooki andmebaasist ei leitud")

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Sisesta mõõt: "))

    hind = koogi_hind(koogi_nimi, koogi_mõõt)

    print(hind)
