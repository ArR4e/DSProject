from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        mõõt1 = pi * mõõt ** 2
        hind1 = mõõt1 * 0.06
        hind_lõpp1 = round(hind1, 2)
        return hind_lõpp1
    elif nimi == "ploomikook":
        mõõt2 = pi * mõõt ** 2
        hind2 = mõõt2 * 0.04
        hind_lõpp2 = round(hind2, 2)
        return hind_lõpp2
    elif nimi == "Napoleoni kook":
        mõõt3 = mõõt ** 2
        hind3 = mõõt3 * 0.10
        hind_lõpp3 = round(hind3, 2)
        return hind_lõpp3
    else:
        raise Exception("Sellist kooki andmebaasis ei leidu")

nimi = input("Sisesta soovitava koogi nimi: ")
mõõt = float(input("Sisesta soovitava koogi mõõt: "))

try:
    lõpphind = koogi_hind(nimi, mõõt)
    print("Teie koogi lõpphind on: ", lõpphind, "eurot.")
except:
    print("Sellist kooki andmebaasist ei leitud")

    
