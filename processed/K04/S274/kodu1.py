from math import pi

def koogi_hind(koogi_nimi,koogi_mõõt):
    if koogi_nimi == "sokolaadikook":
        pindala = pi * koogi_mõõt**2
        hind = pindala * 0.06
        return hind
    elif koogi_nimi == "ploomikook":
        pindala = pi * koogi_mõõt**2
        hind = pindala * 0.04
        return hind
    elif koogi_nimi == "Napoleoni kook":
        pindala = koogi_mõõt**2
        hind = pindala * 0.10
        return hind
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")

koogi_nimi = input("Sisesta koogi nimi: ")
koogi_mõõt = float(input("Sisesta koogi mõõt: "))
print("Koogi hind on: ", round(koogi_hind(koogi_nimi,koogi_mõõt), 2), "eurot.")
    
    