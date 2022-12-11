from math import pi

def koogi_hind(koogi_nimi, mõõt):
    if (koogi_nimi == "šokolaadikook"):
        return round((pi * mõõt**2) * 0.06, 2)
    elif (koogi_nimi == "ploomikook"):
        return round((pi * mõõt**2) * 0.04, 2)
    elif (koogi_nimi == "Napoleoni kook"):
        return round((mõõt**2) * 0.10, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")

while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    mõõt = float(input("Sisesta koogi mõõt: "))
    print("Koogi hind on", koogi_hind(koogi_nimi, mõõt), "€")
    if koogi_nimi == "":
        break
    