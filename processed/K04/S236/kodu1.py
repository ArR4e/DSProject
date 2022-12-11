#1. Pagarikoja kassaaparaat
from math import pi
    
nimi = input("Sisesta koogi nimi:")
mõõt = float(input("Sisesta koogi mõõt:"))

def koogi_hind(nimi, mõõt):
    
    if nimi == "šokolaadikook":
        return (round(pi * (mõõt ** 2) * 0.06), 2)
    elif nimi == "ploomikook":
        return (round(pi * (mõõt ** 2) * 0.04), 2)
    elif nimi == "Napoleoni kook":
        return (round(mõõt * mõõt * 0.10), 2)
    else :
        raise ValueError("Sellist kooki andmebaasist ei leitud.")
    
    
    
