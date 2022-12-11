from math import pi

def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi == "šokolaadikook":
        hind = (pi * mõõt**2) * 0.06
        hind_2 = round(hind, 2)
        print("Koogi hind on ", hind_2, "€")
    elif koogi_nimi == "ploomikook":
        hind = (pi * mõõt**2) * 0.04
        hind_2 = round(hind, 2)
        print("Koogi hind on ", hind_2, "€")
    elif koogi_nimi == "Napoleoni kook":
        hind = (mõõt**2) * 0.10
        hind_2 = round(hind, 2)
        print("Koogi hind on ", hind_2, "€")

        
while True:
    koogi_nimi = input("Koogi nimi: ")
    if koogi_nimi == "":
        break
    if koogi_nimi != "šokolaadikook" and koogi_nimi != "ploomikook" and koogi_nimi != "Napoleoni kook":
        print("Sellist kooki andmebaasis ei leitud")
    else:
        mõõt = input("Koogi mõõt: ")
        #nimi = koogi_nimi
        mõõt = float(mõõt)
        koogi_hind(koogi_nimi, mõõt)