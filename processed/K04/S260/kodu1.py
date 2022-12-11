from math import *

def kookk():
    kook = input("Koogi nimi: ")
    if kook == "":
        return None
    mõõt = float(input("Koogi mõõt: "))
    print(koogi_hind(kook,mõõt))
    kookk()
        
    
def koogi_hind(kook,mõõt):
    if kook.lower() == "šokolaadikook":
        return round(0.06 * pi*(mõõt**2),2)
    if kook.lower() == "ploomikook":
        return round(0.04 * pi*(mõõt**2),2)
    if kook.lower() == "napoleoni kook":
        return round(0.10 * mõõt**2,2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")

kookk()
