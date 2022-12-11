import math

def koogi_hind(nimi, mõõt=0):
    if nimi == "šokolaadikook":
        kook = 0.06
        koogi_pindala = mõõt**2*math.pi
        hind = round(koogi_pindala*kook, 2)
        print("Selle koogi hind on",hind,"eurot.")
        return hind
    elif nimi == "ploomikook":
        kook = 0.04
        koogi_pindala = mõõt**2*math.pi
        hind = round(koogi_pindala*kook, 2)
        print("Selle koogi hind on",hind,"eurot.")
        return hind
    elif nimi == "Napoleoni kook":
        kook = 0.10
        koogi_pindala = mõõt**2
        hind = round(koogi_pindala*kook, 2)
        print("Selle koogi hind on",hind,"eurot.")
        return hind 
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
while True:
    nimi = input("Mis on koogi nimi? ")
    if nimi == "":
        break
    mõõt = float(input("Kui suur on koogi raadius/külg? "))
    koogi_hind(nimi, mõõt)