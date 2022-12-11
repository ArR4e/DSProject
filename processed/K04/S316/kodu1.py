from math import pi

def koogi_hind(kook,mõõt):
    if kook == "šokolaadikook":
        kook = 0.06
        return round(kook * mõõt**2 * pi, 2)
    elif kook == "ploomikook":
        kook = 0.04
        return round(kook * mõõt**2 * pi, 2)
    elif kook == "Napoleoni kook":
        kook = 0.1
        return round(kook * mõõt**2, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
        
while True:
    kook = str(input("Sisesta koogi nimi: "))
    if kook == "":
        break
    else:
        mõõt = float(input("Selle raadius/küljepikkus sentimeetrites: "))
        print(koogi_hind(kook,mõõt))