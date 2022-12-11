from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return round(pi * mõõt ** 2 * 0.06, 2)
    elif nimi == "ploomikook":
        return round(pi * mõõt ** 2 * 0.04, 2)
    elif nimi == "Napoleoni kook":
        return round(mõõt ** 2 * 0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    n = input("Sisesta koogi nimi: ")
    m = float(input("Sisesta koogi mõõt: "))
    if n == "":
        break
    hind = koogi_hind(n, m)
    print("Koogi hind on", hind, "eurot.")