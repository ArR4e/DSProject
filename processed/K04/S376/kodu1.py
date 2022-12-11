from math import pi

koogi_nimi = str(input("Sisesta koogi nimi: "))
koogi_mõõt = float(input("Sisesta koogi mõõt: "))

def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        return round((pi * koogi_mõõt **2) *0.06, 2)
    if koogi_nimi == "ploomikook":
        return round((pi * koogi_mõõt **2) *0.04, 2)
    if koogi_nimi == "Napoleoni kook":
        return round((koogi_mõõt **2) *0.1, 2)
    else:
        raise print("Sellist kooki andmebaasist ei leitud")

while koogi_nimi != "":
    print("Koogi hind on", koogi_hind(koogi_nimi, koogi_mõõt), "eurot.")
    koogi_nimi = str(input("Sisesta koogi nimi: "))
    if koogi_nimi == "":
        break
    koogi_mõõt = float(input("Sisesta koogi mõõt: "))