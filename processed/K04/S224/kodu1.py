from math import pi

def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        return round(((mõõt**2) * pi * 0.06), 2)
    elif nimi == "ploomikook":
        return round(((mõõt**2) * pi * 0.04), 2)
    elif nimi == "Napoleoni kook":
        return round(((mõõt**2) * 0.10), 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud")
    
nimi = input("gimme da cake: ")
mõõt = input("dat big: ")

print(koogi_hind(nimi, float(mõõt)))