from math import pi

def koogi_hind(koogi_nimi, koogi_moot):
    if koogi_nimi == "Napoleoni kook":
        ruutcm1_hind = 0.10
        hind1 = round(ruutcm1_hind * koogi_moot ** 2, 2)
        return hind1
    elif koogi_nimi == "šokolaadikook":
        ruutcm2_hind = 0.06
        hind2 = round(ruutcm2_hind * pi * koogi_moot ** 2, 2)
        return hind2
    elif koogi_nimi == "ploomikook":
        ruutcm2_hind = 0.04
        hind2 = round(ruutcm2_hind * pi * koogi_moot ** 2, 2)
        return hind2
    else:
        return "Sellist kooki andmebaasist ei leitud"

while True:
    koogi_nimi = str(input("Sisesta koogi nimi: "))
    if koogi_nimi == "":
        break
    koogi_moot = float(input("Sisesta koogi mõõt: "))
    print("Koogi hind on ", koogi_hind(koogi_nimi, koogi_moot), "eurot.")