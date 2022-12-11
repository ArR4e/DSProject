import math
def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        mõõt = float(mõõt)
        hind = round((math.pi*mõõt**2*0.06),2)
    elif nimi == "ploomikook":
        mõõt = float(mõõt)
        hind = round((math.pi*mõõt**2*0.04),2)
    elif nimi == "Napoleoni kook":
        mõõt = float(mõõt)
        hind = round((mõõt**2*0.1),2)
    return(hind)

while True:
    kook = input("Sisestage koogi nimi: ")
    if kook == "šokolaadikook" or kook == "ploomikook" or kook == "Napoleoni kook":
        mõõtmed = input("Sisestage koogi mõõtmed: ")
        print("Koogi hind on",koogi_hind(kook,mõõtmed), "eurot.")
    elif kook == "":
        break
    else:
        print("Sellist kooki andmebaasist ei leitud")
    
    
    