from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = 0.06*pi*mõõt**2
    elif nimi == "ploomikook":
        hind = 0.04*pi*mõõt**2
    elif nimi == "Napoleoni kook":
        hind = 0.1*mõõt**2
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind, 2)

while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(nimi, mõõt))