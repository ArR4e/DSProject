from math import pi
while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisesta koogi mõõt: "))
        def koogi_hind(nimi, mõõt):
            if nimi == ("šokolaadikook"):
                return pi * mõõt ** 2 * 0.06
            elif nimi == ("ploomikook"):
                return pi * mõõt ** 2 * 0.04
            elif nimi == ("Napoleoni kook"):
                return mõõt ** 2 * 0.1
            else :
                raise Exception("Sellist kooki andmebaasist ei leitud")
        x = koogi_hind(nimi, mõõt)      
        hind = round(x, 2)
        print("Koogi hind on", hind, "€")