from math import pi

def koogi_hind(kook, mõõt):
    if kook == "Napoleoni kook":
        hind = 0.1 * mõõt * mõõt
    elif kook == "šokolaadikook":
        hind = 0.06 * mõõt * mõõt * pi
    elif kook == "ploomikook":
        hind = 0.04 * mõõt * mõõt * pi
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    
    #return format(hind, ".2f")
    return round(hind, 2)

kook = ""
while True:
    kook = input("Sisestage koogi nimi: ")
    if kook == "":
        break
    mõõt = float(input("Sisestage koogi mõõt: "))
    print(koogi_hind(kook, mõõt))