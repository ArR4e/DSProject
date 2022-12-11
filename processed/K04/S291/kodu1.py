from math import pi

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        koogi_pindala = pi * koogi_mõõt ** 2
        maksumus_eurodes = round(koogi_pindala * 0.06, 2)
        return maksumus_eurodes
    elif koogi_nimi == "ploomikook":
        koogi_pindala = pi * koogi_mõõt ** 2
        maksumus_eurodes = round(koogi_pindala * 0.04, 2)
        return maksumus_eurodes
    elif koogi_nimi == "Napoleoni kook":
        koogi_pindala = koogi_mõõt ** 2
        maksumus_eurodes = round(koogi_pindala * 0.10, 2)
        return maksumus_eurodes
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_nimi.capitalize() + " - hind on " + str(koogi_hind(koogi_nimi, koogi_mõõt)) + " eurot.")

    