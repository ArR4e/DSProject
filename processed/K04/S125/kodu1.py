from math import pi

def koogi_hind(nimi, mõõt):
    mõõt = float(mõõt)
    pindala_ring = pi * (mõõt**2)
    pindala_ruut = mõõt**2
    
    if nimi == "šokolaadikook":
        return round(pindala_ring * 0.06, 2)
    elif nimi == "ploomikook":
        return round(pindala_ring * 0.04, 2)
    elif nimi == "Napoleoni kook":
        return round(pindala_ruut * 0.1, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

        
while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = input("Sisestage koogi mõõt: ")
    hind = koogi_hind(nimi, mõõt)
    print("Koogi hind on: " + str(hind) + " eurot")