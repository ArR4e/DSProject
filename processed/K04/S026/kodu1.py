from math import pi
kook = input("Mis on koogi nimi? ")
mõõt = float(input("Mis on koogi suurus? "))

def koogi_hind():
    if kook != "Šhokolaadikook" or "Ploomikook" or "Napoleoni kook":
        raise Exception("Sellist kooki andmebaasist ei leitud")
    if kook == "Šhokolaadikook":
        pindala = pi * mõõt**2
        hind = pindala * 0.06
        print("Koogi hind on ", round(hind), "eurot")
    if kook == "Ploomikook":
        pindala = pi * mõõt**2
        hind = pindala * 0.04
        print("Koogi hind on ", round(hind), "eurot")
    if kook == "Napoleoni kook":
        pindala = mõõt**2
        hind = pindala * 0.10
        print("Koogi hind on ", round(hind), "eurot")
        
koogi_hind()

#Ma ei oska seda väga rohkem optimiseerida. Kuidagi kindlasti saab :D