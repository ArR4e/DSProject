from math import pi

def koogi_hind(kook, moot):
    try:
        if kook == "šokolaadikook":
            hind = 0.06 * pi * moot**2
        elif kook == "ploomikook":
            hind = 0.04 * pi * moot**2
        elif kook == "Napoleoni kook":
            hind = 0.1 * moot**2
    except:
        return "Sellist kooki andmebaasist ei leitud"
    return round(hind, 2)

#print(koogi_hind("šokolaadikook", 12))

while True:
    kook = input("Sisestage koogi nimi: ")
    if kook == "":
        break
    moot = float(input("Sisestage koogi mõõt sentimeetrites: "))
    print(koogi_hind(kook, moot))