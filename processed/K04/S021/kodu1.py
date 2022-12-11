from math import *

def koogi_hind(nimi, mõõt):
    
    if nimi == "šokolaadikook":
    
        return round(pi*(mõõt**2)*0.06, 2)
    
    elif nimi =="ploomikook":
        
        return round(pi*(mõõt**2)*0.04, 2)

    elif nimi == "Napoleoni kook":
        
        return round(mõõt**2*0.1, 2)

    else:
        raise ValueError("Sellist kooki andmebaasist ei leidu")

while True:
    koogi_nimi = str(input("Sisestage koogi nimi: "))
    
    if koogi_nimi == "":
        break
    else:
        suurus = float(input("Sisestage koogi mõõt: "))
        tulemus=koogi_hind(koogi_nimi, suurus)
    print("Koogi hind on" , tulemus , "eurot")
    continue



