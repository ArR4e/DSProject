from math import *

def koogi_hind(nimi, mõõt):
    
    if nimi == "šokolaadikook":
        return round(pi * mõõt**2 * 0.06, 2)
        
    if nimi == "ploomikook":
        return round(pi * mõõt**2 * 0.04, 2)
        
    if nimi == "Napoleoni kook":
        return round(mõõt**2 * 0.10, 2)
        
while True:       
        
    nimi = str(input("Koogi nimi:"))

    
    if nimi == "šokolaadikook" or nimi == "ploomikook":
        mõõt = float(input("Koogi raadius:"))
        
    elif nimi == "Napoleoni kook":
        mõõt = float(input("Koogi küljepikkus:"))
        
    elif nimi == "":
        break
        
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud.")
    
    hind = str(koogi_hind(nimi, mõõt))
    print("Kook maksab " + hind + " eurot.")
