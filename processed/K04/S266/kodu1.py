from math import*

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        maksumus = (mõõt**2 * pi) * 0.06
    elif nimi == "ploomikook":
        maksumus = (mõõt**2 * pi) * 0.04
    elif nimi == "Napoleoni kook":
        maksumus = mõõt**2 * 0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(maksumus, 2)

while True:
    kook = input("Sisestage koogi nimi: ")
    if kook == "":
        break
    mõõtmed = float(input("Sisestage koogi mõõtmed: "))
    print("Koogi hind on " + str(koogi_hind(kook, mõõtmed)) + " eurot.")
    