import math
def koogi_hind(kook, mõõt):
    if kook == "šokolaadikook":
        pindala=mõõt*mõõt*math.pi
        hind = round(0.06*pindala,2)
        return hind
    elif kook == "ploomikook":
        pindala=mõõt*mõõt*math.pi
        hind = round(0.04*pindala,2)
        return hind
    elif kook == "Napoleoni kook":
        pindala=mõõt*mõõt
        hind = round(0.1*pindala,2)
        return hind
    else:
        raise Exception("Sellist kooki andmebaasis ei leidu.")

kook = str(input("Mis on koogi nimi?:"))
while kook is not "":
    if kook == "Napoleoni kook":
        mõõt = float(input("Mis on koogi külje pikkus?:"))
        #mõõt = külg*külg
        #koogi_hind(kook, mõõt)
        print("Napoleoni koogi hind on ", koogi_hind(kook, mõõt))
    elif kook == "šokolaadikook":
        mõõt = float(input("Mis on koogi raadius?:"))
        #mõõt = raadius*raadius*math.pi
        #koogi_hind(kook, mõõt)
        print("šokolaadikoogi hind on ", koogi_hind(kook, mõõt))
    elif kook == "ploomikook":
        mõõt = float(input("Mis on koogi raadius?:"))
        #mõõt = raadius*raadius*math.pi
        print("Ploomikoogi hind on ", koogi_hind(kook, mõõt))
    else:
        mõõt = float(input("Mis on koogi raadius:"))
        #mõõt = raadius*raadius*math.pi
        print(koogi_hind(kook, mõõt))
    #koogi_hind(kook, mõõt)
    kook = str(input("Mis on koogi nimi?:"))
