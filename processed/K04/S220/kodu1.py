import math


def koogi_hind(kook, mõõt):
    if kook == "šokolaadikook":
        hind = 0.06
        return round(hind * (math.pi *(mõõt)**2),2)
    if kook == "ploomikook":
        hind = 0.04
        return round(hind * (math.pi *(mõõt)**2), 2)
    if kook == "Napoleoni kook":
        hind = 0.10
        return round(hind * (mõõt**2), 2)
    else :
        raise Exception("Sellist kooku andmebaasis ei leitud")

while True :
    kook = input("Sisestage koogi nimi: ")
    if kook == "":
        break
    else :
        mõõt = (float(input("Sisestage koogi mõõt: ")))
        print((koogi_hind(kook, mõõt)))
     
    
        
    
    