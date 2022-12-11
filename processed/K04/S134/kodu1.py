from math import pi
nimi = input("Koogi nimi: ")
mõõt = float(input("Koogi mõõt sentimeetrites: "))
pindala = pi * mõõt * mõõt
npindala = mõõt * mõõt
def koogi_hind(nimi, mõõt):
    while True:
        if nimi == "šokolaadikook":
            return round(pindala * 0.06, 2)
        elif nimi == "ploomikook":
            return round(pindala * 0.04, 2)
        elif nimi == "Napoleoni kook":
            return round(npindala * 0.10, 2)
        elif nimi == "":
            break
        else:
            print("Sellist kooki andmebaasist ei leitud.")
print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot.")
       