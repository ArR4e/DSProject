import math
def koogi_hind(kook, mõõt):
    hind = 0
    if kook == "šokolaadikook":
        hind = round(0.06 * (mõõt**2) * math.pi, 2)
        return hind
    elif kook == "ploomikook":
        hind = round(0.04 * (mõõt**2) * math.pi, 2)
        return hind
    elif kook == "Napoleoni kook":
        hind = round(0.1 * (mõõt**2), 2)
        return hind
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    kook = input(str("Sisesta tahetud kook: "))
    if kook == "":
        break
    mõõt = float(input("Sisesta tahetud koogi mõõtmed: "))
    print("Koogi hind on " + str(koogi_hind(kook, mõõt)) + " eurot")
    