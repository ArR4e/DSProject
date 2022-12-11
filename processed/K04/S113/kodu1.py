from math import pi
nimi = input("Koogi nimi:")
mõõt = float(input("Koogi mõõt:"))

def koogi_hind(nimi, mõõt):
    if nimi == "Šokolaadikook":
        pindala = (pi*mõõt**2)
        return round(0.06*pindala, 2)
    elif nimi == "Ploomikook":
        pindala = (pi*mõõt**2)
        return round(0.04*pindala, 2)
    elif nimi == "Napoleoni kook":
        pindala = (mõõt**2)
        return round(0.1*pindala, 2)

    else:
        print( "Sellist kooki andmebaasis ei leidu!" )
print("Koogi hind on", koogi_hind(nimi, mõõt), "EUR")