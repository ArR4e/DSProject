from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        pindala1 = pi*float(mõõt)**2
        hind1 = 0.06
        return round(hind1*pindala1, 2)
    elif nimi== "ploomikook":
        pindala2 = pi*float(mõõt)**2
        hind2 = 0.04
        return round(hind2*pindala2, 2)
    elif nimi == "napoleoni kook":
        pindala3 = float(mõõt)**2
        hind3 = 0.10
        return round(hind3*pindala3, 2)
    else:
        raise ValueError("Sellist kooki ei leitud andmebaasist.")
    
while True:
    nimi=input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    mõõt=input("Sisesta koogi mõõt sentimeetrites: ")
    print(koogi_hind(nimi.lower(), mõõt), "eurot.")
