from math import pi

hind1 = 0.06
hind2 = 0.04
hind3 = 0.10

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return round(hind1*pindala1, 2)
    elif nimi == "ploomikook":
        return round(hind2*pindala1, 2)
    elif nimi == "Napoleoni kook":
        return round(hind3*pindala2, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
while True:
    nimi = input("Sisestage koogi nimi:")
    if nimi == "":
        break
    mõõt = float(input("Sisesta koogi mõõt:"))
    pindala1 = pi * mõõt**2
    pindala2 = mõõt**2
    print("Koogi hind on", koogi_hind(nimi, mõõt), "eurot")
    








