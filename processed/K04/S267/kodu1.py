from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return round((pi * mõõt**2 * 0.06), 2)
    elif nimi == "ploomikook":
        return round((pi * mõõt**2 * 0.04), 2)
    elif nimi == "Napoleoni kook":
        return round((mõõt**2 * 0.10), 2)
    else:
        raise Exception("Sellist kooki andmebaasis ei leitud")


while True:
    kooginimi = str(input("Sisestage koogi nimi: "))
    if kooginimi == "":
        break
    koogimõõt = float(input("Sisestage koogi mõõt: "))
    try:
        print("Koogi hind on ", (koogi_hind(kooginimi, koogimõõt)), " eurot.")
    except:
        print("Sellist kooki andmebaasis ei leitud.")
    continue