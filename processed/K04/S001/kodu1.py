from math import pi
def koogi_hind(nimi,moot):
    hind = 0
    pindala = 0
    if nimi == "šokolaadikook":
        pindala = pi * (moot**2)
        hind = round(pindala * 0.06, 2)
    elif nimi == "ploomikook":
        pindala = pi * (moot**2)
        hind = round(pindala * 0.04, 2)
    elif nimi == "Napoleoni kook":
        pindala = moot**2
        hind = round(pindala * 0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return hind

while True:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    moot = float(input("Sisesta koogi mõõt: "))
    print("Selle koogi hind on " + str(koogi_hind(nimi,moot)) + " eurot.")