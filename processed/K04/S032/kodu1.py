from math import pi


def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = pi*mõõt**2*0.06
    elif nimi == "ploomikook":
        hind = pi*mõõt**2*0.04
    elif nimi == "Napoleoni kook":
        hind = mõõt*mõõt*0.1
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind,2)
        
while True:    
    kook = input("Mis kooki soovid? ")
    if kook == "":
        break
    mõõt = float(input("Sisesta soovitud suurus: "))
    print("Selle koogi hind on", koogi_hind(kook,mõõt), "eurot.")



